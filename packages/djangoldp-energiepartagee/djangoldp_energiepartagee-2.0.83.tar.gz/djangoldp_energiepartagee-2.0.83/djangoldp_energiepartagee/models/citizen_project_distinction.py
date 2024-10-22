from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import ReadOnly

from djangoldp_energiepartagee.models.citizen_project import CitizenProject


class EarnedDistinction(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Distinction"
    )
    citizen_projects = models.ManyToManyField(
        CitizenProject,
        blank=True,
        verbose_name="Projets Distingués",
        related_name="earned_distinctions",
    )

    class Meta(Model.Meta):
        ordering = ["name"]
        permission_classes = [ReadOnly]  # AuthenticatedOnly
        rdf_type = "energiepartagee:distinction"
        serializer_fields = ["@id", "name"]
        verbose_name = _("Distinction des projets")
        verbose_name_plural = _("Distinctions des projets")

        static_version = 1

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
