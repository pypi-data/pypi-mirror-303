from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.utils import is_anonymous_user

from djangoldp_energiepartagee.models.actor import *
from djangoldp_energiepartagee.permissions import EPRelatedActorPermissions

ROLE_CHOICES = [("admin", "Administrateur"), ("membre", "Membre"), ("refuse", "Refusé")]


class Relatedactor(Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        Actor,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Acteur",
        related_name="members",
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        max_length=50,
        blank=True,
        default="",
        verbose_name="Rôle de l'utilisateur",
    )
    createdate = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création"
    )
    reminderdate = models.DateTimeField(
        blank=True, null=True, verbose_name="Date de relance"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [EPRelatedActorPermissions]
        permission_roles = {
            "member": {"perms": {"view", "add", "change", "delete"}},
            "admin": {"perms": {"view", "add", "change", "delete"}},
        }
        rdf_type = "energiepartagee:relatedactor"
        unique_together = ["user", "actor"]
        verbose_name = _("Membre")
        verbose_name_plural = _("Membres")
        depth = 1

    def __str__(self):
        if self.actor and self.user and self.user.first_name:
            return "%s - %s" % (self.user.first_name, self.actor)
        else:
            return self.urlid

    @classmethod
    def get_mine(cls, user, role=None):
        if is_anonymous_user(user):
            return Relatedactor.objects.none()

        if role is None:
            return Relatedactor.objects.filter(user=user)

        return Relatedactor.objects.filter(user=user, role=role)

    @classmethod
    def get_user_actors_id(cls, user, role=None):
        return cls.get_mine(user=user, role=role).values_list("actor_id", flat=True)
