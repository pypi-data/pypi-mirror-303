from django.conf import settings
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from djangoldp_tamis.models.asset import Asset
from djangoldp_tamis.models.prestation import Prestation
from djangoldp_tamis.models.prestation_step import PrestationStep
from djangoldp_tamis.models.step_to_template import StepToTemplate
from djangoldp_tamis.models.tamis_profile import TamisProfile


@receiver(pre_save, sender=Prestation)
def prestation_reject_without_editorial_work(instance, **kwargs):
    if not instance.editorial_work:
        raise ValidationError({"editorial_work": "Veuillez spécifier une version"})


@receiver(post_save, sender=Prestation)
def prestation_apply_or_create_template_steps(instance, **kwargs):
    if instance.template_steps:
        if instance.template_steps.is_template:
            prestationsteps, created = PrestationStep.objects.get_or_create(
                prestation=instance
            )
            for step in prestationsteps.steps.all():
                step.delete()
            for step in instance.template_steps.steps.all():
                StepToTemplate.objects.create(
                    template=prestationsteps,
                    step=step.step,
                    order=step.order,
                    validated=step.validated,
                    validation_date=step.validation_date,
                )
        instance.template_steps = None
        instance.save()
    else:
        PrestationStep.objects.get_or_create(prestation=instance)


@receiver(post_save, sender=Prestation)
def prestation_create_first_asset(instance, created, **kwargs):
    if created and instance.assets.count() == 0:
        Asset.objects.get_or_create(prestation=instance)


@receiver(post_delete, sender=Prestation)
def prestation_clear_unused_steps(**kwargs):
    PrestationStep.objects.filter(prestation=None, is_template=False).delete()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(instance, **kwargs):
    TamisProfile.objects.get_or_create(user=instance)
