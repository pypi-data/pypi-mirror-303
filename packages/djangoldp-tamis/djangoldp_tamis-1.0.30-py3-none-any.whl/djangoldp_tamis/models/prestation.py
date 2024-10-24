from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import DynamicNestedField, Model
from djangoldp.permissions import (ACLPermissions, AuthenticatedOnly,
                                   ReadAndCreate)
from djangoldp_account.models import LDPUser

from djangoldp_tamis.models.commande import Commande
from djangoldp_tamis.models.editorial_work import EditorialWork
from djangoldp_tamis.models.prestation_step import PrestationStep


class Prestation(Model):
    type = models.CharField(max_length=254, blank=True, null=True, default="")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_prestations",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    template_steps = models.ForeignKey(
        PrestationStep,
        related_name="templated_prestations",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    steps = models.OneToOneField(
        PrestationStep,
        on_delete=models.CASCADE,
        related_name="prestation",
        blank=True,
        null=True,
    )
    admins = models.OneToOneField(
        Group,
        related_name="admin_prestation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    editors = models.OneToOneField(
        Group,
        related_name="editor_prestation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    visitors = models.OneToOneField(
        Group,
        related_name="visitor_prestation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    start_date = models.DateField(
        verbose_name="Date de démarrage", blank=True, null=True
    )
    expected_delivery = models.DateField(
        verbose_name="Date de livraison prévue", blank=True, null=True
    )
    editorial_work = models.ForeignKey(
        EditorialWork,
        on_delete=models.CASCADE,
        related_name="prestations",
        blank=True,
        null=True,
    )
    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name="prestations",
        blank=True,
        null=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            if self.editorial_work.programme.title:
                return "{} - {} ({})".format(
                    self.editorial_work.programme.title, self.type, self.urlid
                )
            if self.editorial_work.programme.season.serie.title:
                return "{} S{}E{} - {} ({})".format(
                    self.editorial_work.programme.season.serie.title,
                    self.programme.season.number,
                    self.programme.number,
                    self.type,
                    self.urlid,
                )
            if self.type:
                return "{} ({})".format(self.type, self.urlid)
            return self.urlid
        except Exception:
            return self.urlid

    class Meta(Model.Meta):
        verbose_name = _("Prestation")
        verbose_name_plural = _("Prestations")

        serializer_fields = [
            "@id",
            "type",
            "start_date",
            "expected_delivery",
            "editorial_work",
            "assets",
            "steps",
            "template_steps",
            "admins",
            "editors",
            "visitors",
            "commande",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["assets", "steps", "admins", "editors", "visitors", "commande"]
        auto_author = "creator"
        rdf_type = "sib:Prestation"
        permission_classes = [AuthenticatedOnly & (ReadAndCreate | ACLPermissions)]
        permission_roles = {
            "admins": {"perms": ["view", "change", "control"], "add_author": True},
            "editors": {"perms": ["view", "change"]},
            "visitors": {"perms": ["view"]},
        }


# add prestations in groups and users
Group._meta.inherit_permissions += [
    "admin_prestation",
    "editor_prestation",
    "visitor_prestation",
]
Group._meta.serializer_fields += [
    "admin_prestation",
    "editor_prestation",
    "visitor_prestation",
]
# TODO: Should take get_user_model instead to handle enventual other OIDC packages?
LDPUser._meta.serializer_fields += ["prestations"]
LDPUser.prestationContainer = lambda self: {"@id": f"{self.urlid}prestations/"}
LDPUser._meta.nested_fields += ["prestations"]
LDPUser.prestations = lambda self: Prestation.objects.filter(
    models.Q(admins__user=self)
    | models.Q(editors__user=self)
    | models.Q(visitors__user=self)
)
LDPUser.prestations.field = DynamicNestedField(Prestation, "prestations")
