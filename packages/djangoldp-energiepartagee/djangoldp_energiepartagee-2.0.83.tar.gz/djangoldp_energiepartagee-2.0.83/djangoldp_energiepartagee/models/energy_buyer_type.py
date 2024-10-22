from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


class ContractType(Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Type")

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:contract_type"
        verbose_name = _("Type de contrat")
        verbose_name_plural = _("Types de contrats")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
