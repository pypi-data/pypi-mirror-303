from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.citizen_project import CitizenProject


class Testimony(Model):
    citizen_project = models.ForeignKey(
        CitizenProject,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Projet",
        related_name="testimonies",
    )
    author_name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Auteur"
    )
    author_picture = models.TextField(
        blank=True, null=True, verbose_name="Auteur: Photo"
    )
    content = models.TextField(
        blank=True, null=True, verbose_name="Contenu"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["citizen_project"]
        rdf_type = "energiepartagee:testimony"
        verbose_name = _("Témoignage")
        verbose_name_plural = _("Témoignages")

    def __str__(self):
        return self.urlid
