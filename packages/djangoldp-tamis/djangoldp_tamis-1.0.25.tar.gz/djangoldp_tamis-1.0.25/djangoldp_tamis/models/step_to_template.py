from datetime import date

from django.db import models
from django.db.models import F, Max
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, InheritPermissions

from djangoldp_tamis.models.prestation_step import PrestationStep
from djangoldp_tamis.models.step import Step


class StepToTemplate(Model):
    template = models.ForeignKey(
        PrestationStep,
        on_delete=models.CASCADE,
        related_name="steps",
        blank=True,
        null=True,
    )
    step = models.ForeignKey(
        Step,
        on_delete=models.CASCADE,
        related_name="templates",
        blank=True,
        null=True,
    )
    order = models.IntegerField(blank=True, null=True)
    validated = models.BooleanField(default=False)
    validation_date = models.DateField(
        verbose_name="Date de validation", blank=True, null=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.order is None:
                max_order = StepToTemplate.objects.filter(
                    template=self.template
                ).aggregate(Max("order"))["order__max"]
                self.order = (max_order + 1) if max_order is not None else 1
            else:
                StepToTemplate.objects.filter(
                    template=self.template, order__gte=self.order
                ).update(order=F("order") + 1)
        else:
            old_order = StepToTemplate.objects.get(pk=self.pk).order
            if self.order is None:
                max_order = StepToTemplate.objects.filter(
                    template=self.template
                ).aggregate(Max("order"))["order__max"]
                self.order = (max_order + 1) if max_order is not None else 1
            if (
                old_order is not None
                and self.order is not None
                and self.order != old_order
            ):
                if self.order > old_order:
                    StepToTemplate.objects.filter(
                        template=self.template,
                        order__gt=old_order,
                        order__lte=self.order,
                    ).update(order=F("order") - 1)
                else:
                    StepToTemplate.objects.filter(
                        template=self.template,
                        order__lt=old_order,
                        order__gte=self.order,
                    ).update(order=F("order") + 1)
        if self.validated and not self.validation_date:
            self.validation_date = date.today()

        super(StepToTemplate, self).save(*args, **kwargs)

    class Meta(Model.Meta):
        verbose_name = _("Prestation Template Step")
        verbose_name_plural = _("Prestation Template Steps")

        serializer_fields = [
            "@id",
            "step",
            "order",
            "validated",
            "validation_date",
            "creation_date",
            "update_date",
        ]
        nested_fields = ["step"]
        rdf_type = "sib:PrestationStep"
        permission_classes = [AuthenticatedOnly & InheritPermissions]
        inherit_permissions = ["template"]
        depth = 1
