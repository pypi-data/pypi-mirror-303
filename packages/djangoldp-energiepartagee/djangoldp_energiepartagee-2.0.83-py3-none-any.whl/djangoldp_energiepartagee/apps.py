from django.apps import AppConfig
from django.conf import settings


class DjangoldpEnergiepartageeConfig(AppConfig):
    name = "djangoldp_energiepartagee"
    if getattr(settings, "IS_AMORCE", False):
        verbose_name = "AMORCE"
    else:
        verbose_name = "Énergie Partagée"
