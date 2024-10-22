from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadAndCreate

from djangoldp_tamis.models.__base import baseEditorialObject


class Serie(baseEditorialObject):

    def __str__(self):
        try:
            if self.title:
                return "{} ({})".format(self.title, self.urlid)
            return "{} ({})".format(
                self.seasons.first().programmes.first().title, self.urlid
            )
        except Exception:
            return self.urlid

    class Meta(Model.Meta):
        verbose_name = _("Serie")
        verbose_name_plural = _("Series")

        serializer_fields = [
            "@id",
            "identifiants",
            "title",
            "alternate_title",
            "seasons",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["identifiants", "seasons"]
        rdf_type = "ec:Series"
        permission_classes = [AuthenticatedOnly & ReadAndCreate]
