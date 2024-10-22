from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions


class EnergyType(Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nom")
    installed_capacity_reference_unit = models.CharField(
        max_length=250, blank=True, null=True
    )
    yearly_proudction_ref_unit = models.CharField(max_length=250, blank=True, null=True)
    capacity_factor_ref_unit = models.CharField(max_length=250, blank=True, null=True)

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["energy_production"]
        rdf_type = "energiepartagee:energy_type"
        verbose_name = _("Type d'énergie")
        verbose_name_plural = _("Types d'énergies")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
