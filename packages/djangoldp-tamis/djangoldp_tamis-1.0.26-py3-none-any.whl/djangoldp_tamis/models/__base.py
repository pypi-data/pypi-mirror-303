from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import ReadOnly

from djangoldp_tamis.models.identifiant import Identifiant


class baseAsset(Model):
    # TODO: Delete on cascade
    identifiants = models.ManyToManyField(
        Identifiant,
        blank=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.urlid

    class Meta(Model.Meta):
        abstract = True
        verbose_name = _("Base Asset")
        verbose_name_plural = _("Base Assets")

        serializer_fields = [
            "@id",
            "identifiants",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["identifiants"]
        rdf_type = "ec:Asset"
        permission_classes = [ReadOnly]


class baseEditorialObject(baseAsset):
    title = models.CharField(max_length=254, blank=True, null=True, default="")
    alternate_title = models.CharField(
        max_length=254, blank=True, null=True, default=""
    )

    def __str__(self):
        if self.title:
            return "{} ({})".format(self.title, self.urlid)
        else:
            return self.urlid

    class Meta(Model.Meta):
        abstract = True
        verbose_name = _("Editorial Object")
        verbose_name_plural = _("Editorial Objects")

        serializer_fields = ["@id", "title", "alternate_title"]
        nested_fields = []
        rdf_type = "ec:EditorialObject"
        permission_classes = [ReadOnly]
