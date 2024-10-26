from django.db import models

# Create your models here.
class EmissionEvents(models.Model):

    # Initialize fields for the Django model storing emission events
    incident_no = models.IntegerField()
    rn =  models.TextField()
    re_name = models.TextField()
    physical_location = models.TextField()
    county = models.TextField()
    tceq_region = models.IntegerField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    event_type = models.TextField()
    emission = models.TextField()
    epn = models.TextField()
    contaminant = models.TextField()
    estimated_quantity = models.DecimalField()
    estimated_ind = models.TextField()
    amount_unk_ind = models.TextField()
    units = models.TextField()
    emissions_limit = models.DecimalField()
    limit_units = models.TextField()
    authorize_comment = models.TextField()
    comment_no = models.IntegerField()
    cause_of_emission = models.TextField()
    action_taken = models.TextField()
    basis_used = models.TextField()
    initial_noti_date = models.DateTimeField()
    hours_elapsed = models.DecimalField()
    emissions_rate = models.DecimalField()
    flag = models.BinaryField()
