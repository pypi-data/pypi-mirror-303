from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, OwnerPermissions, ReadOnly


class TamisProfile(Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tamis_profile"
    )
    enterprise = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=150, blank=True)
    job = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

        auto_author = "user"
        serializer_fields = [
            "@id",
            "enterprise",
            "title",
            "job",
            "phone",
            "creation_date",
            "update_date",
        ]
        nested_fields = []
        rdf_type = "sib:hasStep"
        permission_classes = [OwnerPermissions | (AuthenticatedOnly & ReadOnly)]

    def __str__(self):
        return "{} ({})".format(self.user.get_full_name(), self.user.username)
