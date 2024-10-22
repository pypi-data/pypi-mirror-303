from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model

from djangoldp_energiepartagee.permissions import EPRegionalAdminPermission


class Integrationstep(Model):
    packagestep = models.BooleanField(
        blank=True, null=True, verbose_name="Colis accueil à envoyer", default=False
    )
    adhspacestep = models.BooleanField(
        blank=True, null=True, verbose_name="Non inscrit sur espace Adh", default=False
    )
    adhliststep = models.BooleanField(
        blank=True, null=True, verbose_name="Non inscrit sur liste Adh", default=False
    )
    regionalliststep = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Non inscrit sur liste régional",
        default=False,
    )
    admincomment = models.TextField(
        blank=True, null=True, verbose_name="Commentaires de l'administrateur"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        rdf_type = "energiepartagee:integrationstep"
        permission_classes = [EPRegionalAdminPermission]
        serializer_fields = [
            "packagestep",
            "adhspacestep",
            "adhliststep",
            "regionalliststep",
            "admincomment",
        ]
        verbose_name = _("Étapes d'intégration")
        verbose_name_plural = _("Étapes d'intégration")

    def __str__(self):
        return str(self.id)
