from django.conf import settings
from django.db.models.signals import post_delete, post_save, pre_save
from django.db.transaction import on_commit
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from djangoldp_tamis.models.asset import Asset
from djangoldp_tamis.models.prestation import Prestation
from djangoldp_tamis.models.prestation_step import PrestationStep
from djangoldp_tamis.models.step import Step
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


@receiver(post_save, sender=PrestationStep)
def ensure_prestationstep_laststeps(instance, **kwargs):
    def on_commit_steps():
        LIVRAISON_STEP = Step.objects.get_or_create(name="Livraison")[0]
        VALIDATION_STEP = Step.objects.get_or_create(name="Validation")[0]

        last_two_steps = instance.steps.order_by('-order')[:2]
        before_last_step = last_two_steps[1] if len(last_two_steps) > 1 else StepToTemplate()
        last_step = last_two_steps[0] if len(last_two_steps) > 0 else StepToTemplate()

        if last_step.step != VALIDATION_STEP or (last_step.step == VALIDATION_STEP and not last_step.validated):
            if before_last_step.step == LIVRAISON_STEP:
                StepToTemplate.objects.filter(template=instance, step=LIVRAISON_STEP, validated=False).exclude(order=before_last_step.order).delete()
            else:
                StepToTemplate.objects.filter(template=instance, step=LIVRAISON_STEP, validated=False).delete()
                before_last_step = StepToTemplate.objects.create(template=instance, step=LIVRAISON_STEP)

            if last_step.step == VALIDATION_STEP:
                StepToTemplate.objects.filter(template=instance, step=VALIDATION_STEP, validated=False).exclude(order=last_step.order).delete()
            else:
                StepToTemplate.objects.filter(template=instance, step=VALIDATION_STEP, validated=False).delete()
                last_step = StepToTemplate.objects.create(template=instance, step=VALIDATION_STEP)

            if before_last_step.order is not None and last_step.order is not None and before_last_step.order > last_step.order:
                before_last_step.order = last_step.order
                before_last_step.save()

    on_commit(on_commit_steps)


@receiver(post_save, sender=PrestationStep)
def fix_prestationsteps_order(instance, **kwargs):
    def on_commit_steps():
        order = 0
        for step in instance.steps.order_by('order'):
            order += 1
            if step.order != order:
                step.order = order
                step.save()

    on_commit(on_commit_steps)


@receiver(post_save, sender=StepToTemplate)
def add_steps_after_deny(instance, created, **kwargs):
    deny = Step.objects.get_or_create(name="Refusé")[0]
    if created and instance.step == deny:
        validation = Step.objects.get_or_create(name="Validation")[0]
        livraison = Step.objects.get_or_create(name="Livraison")[0]

        StepToTemplate.objects.create(template=instance.template, step=validation)
        StepToTemplate.objects.create(template=instance.template, step=livraison)
