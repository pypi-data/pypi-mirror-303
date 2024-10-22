from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import ReadOnly

from djangoldp_energiepartagee.permissions import EPRegionalAdminPermission


class Region(Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Région")
    isocode = models.CharField(
        max_length=6, blank=True, null=True, verbose_name="code ISO"
    )
    acronym = models.CharField(
        max_length=6, blank=True, null=True, verbose_name="Acronyme"
    )
    admins = models.ManyToManyField(get_user_model(), related_name="admin_regions", blank=True, verbose_name="Super Admins")

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [ReadOnly | EPRegionalAdminPermission]
        rdf_type = "energiepartagee:region"
        serializer_fields = ["name", "isocode", "acronym"]
        verbose_name = _("Région")
        verbose_name_plural = _("Régions")
        static_version = 1

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
