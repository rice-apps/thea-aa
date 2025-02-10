from django.urls import path, include
from .models import EmissionEvents, SuperfundSite
from rest_framework.serializers import ModelSerializer

class EmissionEventSerializer(ModelSerializer):
    class Meta:
        model = EmissionEvents
        fields = ['re_name',
            'physical_location',
            'start_date_time',
            'end_date_time',
            'contaminant',
            'estimated_quantity',
            'emissions_limit',
            'limit_units',
            'hours_elapsed',
            'emissions_rate',
            'flag'
            ]
        

class SuperfundSiteSerializer(ModelSerializer):
    class Meta:
        model = SuperfundSite
        fields = ['epa_id',
                  'site_name',
                  'city',
                  'county',
                  'state',
                  'street_address',
                  'zip_code',
                  'region',
                  'npl_status',
                  'partial_npl_deletion',
                  'superfund_alternative_approach',
                  'site_wide_ready_for_anticipated_use',
                  'human_exposure_under_control',
                  'groundwater_migration_under_control',
                  'construction_complete',
                  'construction_completion_date',
                  'non_npl_status_category',
                  'non_npl_status_subcategory',
                  'site_status',
                  'site_type',
                  'site_type_subcategory',
                  'federal_agency',
                  'native_american_interest',
                  'indian_entity_nai_status',
                  'hrs_score',
                  'federal_facility_indicator',
                  'alias_alternative_site_name',
                  'non_npl_status_date',
                  'superfund_site_profile_page_url',
                  'rcra_handler_id_name',
                  'latitude',
                  'longitude'
                  ]