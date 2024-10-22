from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


class Paymentmethod(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Mode de paiement"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:paymentmethod"
        serializer_fields = ["name"]
        verbose_name = _("Méthode de paiement")
        verbose_name_plural = _("Méthodes de paiements")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
