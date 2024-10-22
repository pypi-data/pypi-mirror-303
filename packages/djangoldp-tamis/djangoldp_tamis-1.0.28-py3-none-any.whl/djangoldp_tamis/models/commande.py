from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly

from djangoldp_tamis.models.identifiant import Identifiant


class Commande(Model):
    title = models.CharField(max_length=254, blank=True, null=True, default="")
    client_name = models.CharField(max_length=254, blank=True, null=True, default="")
    # TODO: Delete on cascade
    identifiants = models.ManyToManyField(
        Identifiant,
        blank=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return "{} ({})".format(self.title, self.urlid)
        else:
            return self.urlid

    class Meta(Model.Meta):
        verbose_name = _("Commande")
        verbose_name_plural = _("Commandes")

        serializer_fields = [
            "@id",
            "title",
            "client_name",
            "identifiants",
            "prestations",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["identifiants", "prestations"]
        rdf_type = "sib:Commande"
        permission_classes = [AuthenticatedOnly]
