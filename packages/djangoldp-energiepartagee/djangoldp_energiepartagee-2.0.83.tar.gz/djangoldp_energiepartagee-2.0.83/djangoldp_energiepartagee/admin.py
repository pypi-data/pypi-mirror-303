from django.conf import settings
from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin

from djangoldp_energiepartagee.models import *


@admin.register(
    CommunicationProfile,
    SAPermission,
    Testimony,
)
class EmptyAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(
    College,
    Collegeepa,
    Integrationstep,
    Interventionzone,
    Legalstructure,
    Paymentmethod,
    Profile,
    EnergyBuyer,
    EnergyType,
    EnergyProduction,
    ContractType,
    PartnerLink,
    PartnerLinkType,
)
class EPModelAdmin(DjangoLDPAdmin):
    readonly_fields = ("urlid",)
    exclude = ("is_backlink", "allow_create_backlink")
    extra = 0


@admin.register(Regionalnetwork)
class EPRegionalnetworkAdmin(EPModelAdmin):
    filter_horizontal = ("colleges",)


@admin.register(Region)
class EPRegionAdmin(EPModelAdmin):
    filter_horizontal = ("admins",)


@admin.register(EarnedDistinction)
class EPDistinctionAdmin(EPModelAdmin):
    filter_horizontal = ("citizen_projects",)


@admin.register(SiteEarnedDistinction)
class EPSiteEarnedDistinctionAdmin(EPModelAdmin):
    filter_horizontal = ("production_sites",)


class TestimonyInline(admin.TabularInline):
    model = Testimony
    fk_name = "citizen_project"
    exclude = ("urlid", "is_backlink", "allow_create_backlink")
    extra = 0


class CommunicationProfileInline(admin.StackedInline):
    model = CommunicationProfile
    fk_name = "citizen_project"
    exclude = ("urlid", "is_backlink", "allow_create_backlink")
    extra = 0


@admin.register(CitizenProject)
class CitizenProjectAdmin(EPModelAdmin):
    list_display = ("urlid", "founder", "name", "created_at", "updated_at")
    list_filter = (
        "status",
        "region",
        "visible",
        ("lat", admin.EmptyFieldListFilter),
        ("lng", admin.EmptyFieldListFilter),
    )
    search_fields = ["urlid", "name", "founder__longname", "founder__shortname"]
    ordering = [ "founder__longname", "name"]
    inlines = [CommunicationProfileInline, TestimonyInline]


@admin.register(CapitalDistribution)
class CapitalDistributionAdmin(EPModelAdmin):
    search_fields = ["actor__longname", "actor__shortname"]
    ordering = [ "actor__longname"]

@admin.register(Shareholder)
class ShareholderAdmin(EPModelAdmin):
    list_display =("capital_distribution", "actor")
    search_fields = ["capital_distribution__actor__longname", "capital_distribution__actor__shortname", "actor__longname", "actor__shortname"]
    ordering = [ "capital_distribution__actor__longname"]
    

@admin.register(ProductionSite)
class ProductionSiteAdmin(EPModelAdmin):
    list_display = ("urlid", "name", "project", "actor", "created_at", "updated_at")
    list_filter = (
        "progress_status",
        "region",
        "visible",
        ("lat", admin.EmptyFieldListFilter),
        ("lng", admin.EmptyFieldListFilter),
    )
    exclude = ("is_backlink", "allow_create_backlink", "old_visible")
    search_fields = [
        "urlid",
        "name",
        "citizen_project__name",
        "citizen_project__founder__longname",
        "citizen_project__founder__shortname",
    ]
    ordering = ["name"]

    def project(self, obj):
        return obj.citizen_project.name

    def actor(self, obj):
        return obj.citizen_project.founder.longname


@admin.register(Actor)
class ActorAdmin(EPModelAdmin):
    list_display = ("urlid", "longname", "shortname", "updatedate", "createdate")
    list_filter = (
        "actortype",
        "category",
        "region",
        "visible",
        ("lat", admin.EmptyFieldListFilter),
        ("lng", admin.EmptyFieldListFilter),
        "status",
    )
    search_fields = ["longname", "shortname"]
    ordering = ["longname"]
    filter_horizontal = ("interventionzone",)


@admin.register(Relatedactor)
class RelatedactorAdmin(EPModelAdmin):
    list_display = ("__str__", "role")
    search_fields = [
        "actor__longname",
        "actor__shortname",
        "user__first_name",
        "user__last_name",
        "user__email",
    ]


if not getattr(settings, "IS_AMORCE", False):

    @admin.register(Contribution)
    class ContributionAdmin(EPModelAdmin):
        list_display = ("actor", "year", "updatedate", "createdate")
        search_fields = ["actor__longname", "actor__shortname"]
        filter_horizontal = ("discount",)

        def get_readonly_fields(self, request, obj=None):
            if obj and obj.contributionstatus in (
                "a_ventiler",
                "valide",
            ):
                return self.readonly_fields + ("amount",)
            return self.readonly_fields

else:

    admin.site.register(Contribution, EmptyAdmin)
