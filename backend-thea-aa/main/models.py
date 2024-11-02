from django.db import models

<<<<<<< HEAD
# Create your models here.
class EmissionEvents(models.Model):

    # Initialize fields for the Django model storing emission events
    re_name = models.TextField()
    physical_location = models.TextField()
    start_date_time = models.TextField()
    end_date_time = models.TextField()
    contaminant = models.TextField()
    estimated_quantity = models.TextField()
    emissions_limit = models.TextField()
    limit_units = models.TextField()
    hours_elapsed = models.TextField()
    emissions_rate = models.TextField()
    flag = models.IntegerField()
=======
class SuperfundSite(models.Model):
    epa_id = models.CharField()
    site_name = models.TextField() 
    city = models.CharField()
    county = models.CharField()
    state = models.CharField()
    street_address = models.TextField()
    zip_code = models.CharField()
    region = models.IntegerField()
    npl_status = models.CharField()
    partial_npl_deletion = models.BooleanField()
    superfund_alternative_approach = models.BooleanField()
    site_wide_ready_for_anticipated_use = models.BooleanField()
    human_exposure_under_control = models.BooleanField()
    groundwater_migration_under_control = models.BooleanField()
    construction_complete = models.BooleanField()
    construction_completion_date = models.DateTimeField()  
    non_npl_status_category = models.CharField()
    non_npl_status_subcategory = models.CharField()
    non_npl_status = models.CharField()
    site_status = models.CharField()
    site_type = models.CharField()
    site_type_subcategory = models.CharField()
    federal_agency = models.TextField() 
    native_american_interest = models.BooleanField()
    indian_entity_nai_status = models.CharField()
    hrs_score = models.DecimalField()  
    federal_facility_indicator = models.BooleanField()
    alias_alternative_site_name = models.TextField()
    non_npl_status_date = models.DateTimeField()  
    superfund_site_profile_page_url = models.URLField()
    rcra_handler_id = models.CharField()
    rcra_handler_name = models.TextField() 
>>>>>>> origin/scrape-superfund
