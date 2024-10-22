from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


class College(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="collège"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:college"
        serializer_fields = ["name"]
        verbose_name = _("Collège")
        verbose_name_plural = _("Collèges")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
