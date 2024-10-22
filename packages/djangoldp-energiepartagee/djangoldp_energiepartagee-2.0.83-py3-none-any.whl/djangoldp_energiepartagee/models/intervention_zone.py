from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


class Interventionzone(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Zone d'intervention"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:interventionzone"
        serializer_fields = ["name"]
        verbose_name = _("Zone d'intervention")
        verbose_name_plural = _("Zones d'interventions")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
