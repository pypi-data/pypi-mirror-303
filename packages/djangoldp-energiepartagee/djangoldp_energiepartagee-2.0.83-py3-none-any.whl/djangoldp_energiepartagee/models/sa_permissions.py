from djangoldp.models import Model

from djangoldp_energiepartagee.permissions import EPContributionPermission

# Workaround to avoid /contributions/ call for super-admin checks

class SAPermission(Model):
    class Meta(Model.Meta):
        permission_classes = [EPContributionPermission]
        rdf_type = "energiepartagee:permission"
        depth = 0
