from django.urls import path, include
from .models import EmissionEvents, SuperfundSite
from rest_framework.serializers import ModelSerializer

class EmissionEventSerializer(ModelSerializer):
    class Meta:
        model = EmissionEvents
        fields = ['registration',
            're_name',
            'physical_location',
            'region_id',
            'event_type',
            'emission_point_name',
            'epn',
            'start_date_time',
            'end_date_time',
            'contaminant',
            'contaminant_est_quantity',
            'contaminant_est_quantity_units',
            'contaminant_emissions_limit',
            'contaminant_emissions_limit_units',
            'authorization',
            'hours_elapsed',
            'emissions_rate',
            'authorization_comment',
            'cause',
            'actions_taken',
            'basis_used',
            'initial_notice',
            'flag']
        

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
                  'lon',
                  'lat',
                  ]