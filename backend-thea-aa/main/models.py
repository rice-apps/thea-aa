from django.db import models

# Create your models here.

# TODO: parse text to create boolean fields, debug issues with decimal fields

class EmissionEvents(models.Model):

    # Initialize fields for the Django model storing emission events
    registration = models.TextField()
    re_name = models.TextField()
    physical_location = models.TextField()
    region_id = models.TextField()
    event_type = models.TextField()
    emission_point_name = models.TextField()
    epn = models.TextField()
    start_date_time = models.TextField()
    end_date_time = models.TextField()
    contaminant = models.TextField()
    
    # Fields for estimated contaminant table data
    contaminant_est_quantity = models.TextField() 
    contaminant_est_quantity_units = models.TextField(default="")
    contaminant_emissions_limit = models.TextField()  
    contaminant_emissions_limit_units = models.TextField()  
    authorization = models.TextField(default="")
    
    hours_elapsed = models.TextField()
    emissions_rate = models.TextField()
    authorization_comment = models.TextField()
    cause = models.TextField()
    actions_taken = models.TextField()
    basis_used = models.TextField()
    initial_notice = models.TextField()
    flag = models.CharField(max_length = 1)



class SuperfundSite(models.Model):

    epa_id = models.CharField(max_length=12, unique=True)
    site_name = models.TextField() 
    city = models.TextField()
    county = models.TextField()
    state = models.CharField(max_length=2)
    street_address = models.TextField()
    zip_code = models.CharField(max_length=5)
    region = models.TextField()
    npl_status = models.TextField()
    partial_npl_deletion = models.TextField()
    superfund_alternative_approach = models.TextField()
    site_wide_ready_for_anticipated_use = models.TextField()
    human_exposure_under_control = models.TextField()
    groundwater_migration_under_control = models.TextField()
    construction_complete = models.TextField()
    construction_completion_date = models.TextField()  
    non_npl_status_category = models.TextField()
    non_npl_status_subcategory = models.TextField()
    non_npl_status = models.TextField()
    site_status = models.TextField()
    site_type = models.TextField()
    site_type_subcategory = models.TextField()
    federal_agency = models.TextField() 
    native_american_interest = models.TextField()
    indian_entity_nai_status = models.TextField()
    hrs_score = models.TextField()  
    federal_facility_indicator = models.TextField()
    alias_alternative_site_name = models.TextField()
    non_npl_status_date = models.TextField()  
    superfund_site_profile_page_url = models.TextField()
    rcra_handler_id_name = models.TextField() 
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
