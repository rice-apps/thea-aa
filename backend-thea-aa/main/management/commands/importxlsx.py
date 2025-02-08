# management/commands/import_products.py
from django.core.management.base import BaseCommand
import pandas as pd
from main.models import SuperfundSite, EmissionEvents

def import_emission_events(file_path):
    df = pd.read_excel(file_path)

    emission_events = [EmissionEvents(
                            re_name = row['RE NAME'],
                            physical_location = row['PHYSICAL LOCATION'],
                            start_date_time = row['START DATE/TIME'],
                            end_date_time = row['END DATE/TIME'],
                            contaminant = row['CONTAMINANT'],
                            contaminant_est_quantity = row['EST QUANTITY/OPACITY'],
                            contaminant_est_quantity_units = row['UNITS'],
                            contaminant_emissions_limit = row['EMISSION LIMIT'],
                            contaminant_emissions_limit_units = row['LIMIT UNITS'],
                            authorization = row['AUTHORIZATION COMMENT'],
                            hours_elapsed = row['Hours Elapsed:'],
                            emissions_rate = row['Emissions Rate (lbs/hr):'],
                            flag = row['Flag(Y/N):']) for _, row in df.iterrows()]
    
    EmissionEvents.objects.bulk_create(emission_events)

def import_superfund_sites(file_path):
    df = pd.read_excel(file_path)

    superfund_sites = [SuperfundSite(
            epa_id = row['EPA ID'],
            site_name = row['Site Name'],
            city = row['City'],
            county = row['County'],
            state = row['State'],
            street_address = row['Street Address'],
            zip_code = row['Zip Code'],
            region = row['Region'],
            npl_status = row['NPL Status'],
            partial_npl_deletion = row['Partial NPL Deletion'],
            superfund_alternative_approach = row['Superfund Alternative Approach'],
            site_wide_ready_for_anticipated_use = row['Site-wide Ready for Anticipated Use'],
            human_exposure_under_control = row['Human Exposure Under Control'],
            groundwater_migration_under_control = row['Groundwater Migration Under Control'],
            construction_complete = row['Construction Complete'],
            construction_completion_date = row['Construction Completion Date'],
            non_npl_status_category = row['Non-NPL Status Category'],
            non_npl_status_subcategory = row['Non-NPL Status Subcategory'],
            non_npl_status = row['Non-NPL Status'],
            site_status = row['Site Status'],
            site_type = row['Site Type'],
            site_type_subcategory = row['Site Type Subcategory'],
            federal_agency = row['Federal Agency'],
            native_american_interest = row['Native American Interest (NAI)'],
            indian_entity_nai_status = row['Indian Entity (NAI Status)'],
            hrs_score = row['HRS Score'],
            federal_facility_indicator = row['Federal Facility Indicator'],
            alias_alternative_site_name = row['Alias/Alternative Site Name'],
            non_npl_status_date = row['Non-NPL Status Date'],
            superfund_site_profile_page_url = row['Superfund Site Profile Page URL'],
            rcra_handler_id_name = row['RCRA Handler ID - RCRA Handler Name']) for _, row in df.iterrows()]
    
    SuperfundSite.objects.bulk_create(superfund_sites)

class Command(BaseCommand):
    help = 'Import emission event data from Excel file'

    def handle(self, *args, **options):
        superfund_path = 'main/data/superfund.xlsx'
        emission_path = 'main/data/tceq_data.xlsx'

        import_emission_events(emission_path)
        import_superfund_sites(superfund_path)