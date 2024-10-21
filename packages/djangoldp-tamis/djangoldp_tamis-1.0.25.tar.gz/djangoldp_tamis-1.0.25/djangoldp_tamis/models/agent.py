from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly


class Agent(Model):
    name = models.CharField(max_length=254, blank=True, null=True, default="")
    short_name = models.CharField(max_length=254, blank=True, null=True, default="")
    dbpedia = models.CharField(max_length=254, blank=True, null=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name:
            return "{} ({})".format(self.name, self.urlid)
        else:
            return self.urlid

    class Meta(Model.Meta):
        verbose_name = _("Agent")
        verbose_name_plural = _("Agents")

        serializer_fields = [
            "@id",
            "name",
            "short_name",
            "dbpedia",
            "creation_date",
            "update_date",
        ]
        nested_fields = []
        rdf_type = "ec:Agent"
        permission_classes = [AuthenticatedOnly]
