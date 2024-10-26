from django.db import models

# Create your models here.
class EmissionEvents(models.Model):

    # Initialize fields for the Django model storing emission events
    re_name = models.TextField()
    physical_location = models.TextField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    contaminant = models.TextField()
    estimated_quantity = models.DecimalField()
    emissions_limit = models.DecimalField
    limit_units = models.TextField()
    hours_elapsed = models.DecimalField()
    emissions_rate = models.DecimalField()
    flag = models.BinaryField()