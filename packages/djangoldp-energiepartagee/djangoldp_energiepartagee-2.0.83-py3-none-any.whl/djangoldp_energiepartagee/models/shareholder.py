from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.actor import Actor
from djangoldp_energiepartagee.models.capital_distribution import \
    CapitalDistribution


class Shareholder(Model):
    actor = models.ForeignKey(
        Actor,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Actionnaire",
        related_name="shareholders",
    )
    capital_distribution = models.ForeignKey(
        CapitalDistribution,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Acteur",
        related_name="shareholders",
    )
    capital_amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Montant capital",
    )
    other_funds_amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Montant autres fonds",
    )
    relay_investment = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Investissement relais",
        default=False,
    )

    @property
    def capital_amount_percentage(self):
        if self.capital_amount:
            return round(
                self.capital_amount / self.capital_distribution.total_capital * 100, 2
            )
        return 0

    @property
    def other_funds_amount_percentage(self):
        if self.other_funds_amount:
            return round(
                self.other_funds_amount / self.capital_distribution.total_other_funds * 100,
                2,
            )
        return 0

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["capital_distribution"]
        rdf_type = "energiepartagee:shareholder"
        serializer_fields = [
            "actor",
            "capital_distribution",
            "capital_amount",
            "other_funds_amount",
            "relay_investment",
            "capital_amount_percentage",
            "other_funds_amount_percentage",
        ]
        verbose_name = _("Actionnaire")
        verbose_name_plural = _("Actionnaires")

    def __str__(self):
        if self.actor and self.capital_distribution:
            if self.actor.longname and self.capital_distribution.actor:
                if self.capital_distribution.actor.longname:
                    return "Actor {} - Shareholder {}".format(
                        self.capital_distribution.actor.longname, self.actor.longname
                    )
        return self.urlid
