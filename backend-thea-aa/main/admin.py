from django.contrib import admin
from .models import EmissionEvents, SuperfundSite

# Register your models here.
admin.site.register(EmissionEvents)
admin.site.register(SuperfundSite)