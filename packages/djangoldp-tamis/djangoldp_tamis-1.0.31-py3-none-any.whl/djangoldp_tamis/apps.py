from django.apps import AppConfig


class DjangoldpTamisConfig(AppConfig):
    name = "djangoldp_tamis"

    def ready(self):
        from djangoldp_tamis.models.step import Step

        Step.objects.get_or_create(name="Refusé")
        Step.objects.get_or_create(name="Validation")
        Step.objects.get_or_create(name="Livraison")
