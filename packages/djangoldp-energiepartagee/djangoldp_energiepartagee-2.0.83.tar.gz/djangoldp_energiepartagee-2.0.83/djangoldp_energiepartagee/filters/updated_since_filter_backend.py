from rest_framework import filters
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

class UpdatedSinceFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        updated_since = request.query_params.get('since')
        if not updated_since:
            print("No updated_since parameter", queryset)
            return queryset.none()

        try:
            updated_since = timezone.datetime.fromisoformat(updated_since)
        except ValueError:
            print("Invalid updated_since parameter")
            return queryset.none()

        from djangoldp_energiepartagee.models import ProductionSite, EnergyProduction
        # Get projects updated or created directly
        projects = queryset.filter(Q(updated_at__gte=updated_since) | Q(created_at__gte=updated_since))

        # Get projects with updated or newly created production sites
        production_sites = ProductionSite.objects.filter(Q(updated_at__gte=updated_since) | Q(created_at__gte=updated_since))
        projects_from_sites = queryset.filter(production_sites__in=production_sites)

        # Get projects with updated or newly created energy productions
        energy_productions = EnergyProduction.objects.filter(Q(updated_at__gte=updated_since) | Q(created_at__gte=updated_since))
        production_sites_from_energy = ProductionSite.objects.filter(energy_productions__in=energy_productions)
        projects_from_energy = queryset.filter(production_sites__in=production_sites_from_energy)

        # Combine all queries using | operator to remove duplicates
        all_projects = projects | projects_from_sites | projects_from_energy

        return all_projects.distinct()