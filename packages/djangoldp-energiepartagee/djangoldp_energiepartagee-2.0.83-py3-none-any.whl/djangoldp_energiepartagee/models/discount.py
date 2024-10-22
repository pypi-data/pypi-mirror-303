from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoldp.models import Model
from djangoldp.permissions import ReadOnly, AuthenticatedOnly


class Discount(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Nom de la réduction"
    )
    amount = models.DecimalField(
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        verbose_name="Montant de la réduction (%)",
    )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:discount"
        serializer_fields = ["name", "amount"]
        verbose_name = _("Réduction")
        verbose_name_plural = _("Réductions")
