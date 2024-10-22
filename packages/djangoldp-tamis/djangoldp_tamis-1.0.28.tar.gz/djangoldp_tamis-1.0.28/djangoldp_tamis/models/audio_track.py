from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadAndCreate

from djangoldp_tamis.models.__base import baseAsset


class AudioTrack(baseAsset):
    # TODO: http://www.ebu.ch/metadata/ontologies/ebucoreplus#AudioTrack
    audio_channel_number = models.CharField(
        max_length=254, blank=True, null=True, default=""
    )
    bit_depth = models.CharField(max_length=254, blank=True, null=True, default="")
    sample_rate = models.CharField(max_length=254, blank=True, null=True, default="")

    class Meta(Model.Meta):
        verbose_name = _("Audio Track")
        verbose_name_plural = _("Audio Tracks")
        serializer_fields = [
            "@id",
            "identifiants",
            "audio_channel_number",
            "bit_depth",
            "sample_rate",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["identifiants"]
        rdf_type = "ec:AudioTrack"
        permission_classes = [AuthenticatedOnly & ReadAndCreate]
