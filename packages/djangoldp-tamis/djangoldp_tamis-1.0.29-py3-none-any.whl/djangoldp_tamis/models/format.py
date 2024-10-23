from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadAndCreate


class Format(Model):
    # TODO: http://www.ebu.ch/metadata/ontologies/ebucoreplus#FileFormat
    identifier = models.CharField(max_length=254, blank=True, null=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.identifier:
            return "{} ({})".format(self.identifier, self.urlid)
        else:
            return self.urlid

    class Meta(Model.Meta):
        verbose_name = _("File Format")
        verbose_name_plural = _("File Formats")
        serializer_fields = [
            "@id",
            "identifier",
            "creation_date",
            "update_date",
        ]
        nested_fields = []
        rdf_type = "ec:FileFormat"
        permission_classes = [AuthenticatedOnly & ReadAndCreate]
