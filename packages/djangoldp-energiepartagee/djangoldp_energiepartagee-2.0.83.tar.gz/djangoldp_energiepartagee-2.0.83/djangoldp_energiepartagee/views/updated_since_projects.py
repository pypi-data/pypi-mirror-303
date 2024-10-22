from datetime import datetime

from djangoldp.views import LDPViewSet
from djangoldp_energiepartagee.models import CitizenProject
from djangoldp_energiepartagee.filters import UpdatedSinceFilterBackend


class UpdatedSinceProjectsViewset(LDPViewSet):
    model = CitizenProject
    queryset = CitizenProject.objects.none()
    filter_backends = [UpdatedSinceFilterBackend]
