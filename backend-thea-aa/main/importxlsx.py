# management/commands/import_products.py
from django.core.management.base import BaseCommand
import pandas as pd
from main.models import EmissionEvents

def import_data(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        EmissionEvents.objects.create(
            re_name = row['RE NAME'],
            physical_location = row['PHYSICAL LOCATION'],
            start_date_time = row['START DATE/TIME'],
            end_date_time = row['END DATE/TIME'],
            contaminant = row['CONTAMINANT'],
            estimated_quantity = row['EST QUANTITY/OPACITY'],
            emissions_limit = row['EMISSION LIMIT'],
            limit_units = row['LIMIT UNITS'],
            hours_elapsed = row['Hours Elapsed:'],
            emissions_rateg = row['Emissions Rate (lbs/hr):'],
            flag = row['Flag(Y/N):'],
        )

class Command(BaseCommand):
    help = 'Import emission event data from Excel file'

    def handle(self, *args, **options):
        file_path = 'main/data/example.xlsx'
        import_data(file_path)