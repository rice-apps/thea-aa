from django.db import models

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
