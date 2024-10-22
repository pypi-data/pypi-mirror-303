from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions



class EnergyBuyer(Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nom")

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["energy_bought"]
        rdf_type = "energiepartagee:energy_buyer"
        verbose_name = _("Acheteur d'énergie")
        verbose_name_plural = _("Acheteurs d'énergies")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
