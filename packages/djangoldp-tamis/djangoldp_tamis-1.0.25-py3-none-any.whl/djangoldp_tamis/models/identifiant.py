from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly

from djangoldp_tamis.models.agent import Agent


class Identifiant(Model):
    # TODO: http://www.ebu.ch/metadata/ontologies/ebucoreplus#Identifier
    identifier = models.CharField(max_length=254, blank=True, null=True, default="")
    issuer = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.identifier:
            return "{} ({})".format(self.identifier, self.urlid)
        else:
            return self.urlid

    class Meta(Model.Meta):
        verbose_name = _("Identifiant")
        verbose_name_plural = _("Identifiants")

        serializer_fields = [
            "@id",
            "identifier",
            "issuer",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["issuer"]
        rdf_type = "ec:Identifier"
        permission_classes = [AuthenticatedOnly]
