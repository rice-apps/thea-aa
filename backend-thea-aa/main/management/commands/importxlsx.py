# management/commands/import_products.py
from django.core.management.base import BaseCommand
import pandas as pd
from main.models import SuperfundSite, EmissionEvents

def import_emission_events(file_path):
    df = pd.read_excel(file_path)
    
    emission_events = [EmissionEvents(
                            registration = row['RN'],
                            re_name = row['RE NAME'],
                            physical_location = row['PHYSICAL LOCATION'],
                            region_id = row['TCEQ REGION'],
                            # event_type = row['EVENT_TYPE'],
                            emission_point_name = row['EMISSION POINT NAME'],
                            epn = row['EPN'],
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
                            authorization_comment = row['AUTHORIZATION COMMENT'],
                            cause = row['Cause of Emission Event'],
                            actions_taken = row['Actions Taken'],
                            basis_used = row['Basis Used to Determine Quantities and Any Additional Information Necessary to Evaluate the Event'],
                            initial_notice = row['Initial Notification:'],
                            flag = row['Flag(Y/N):']) for _, row in df.iterrows()]
    
    
    
    EmissionEvents.objects.bulk_create(emission_events)

def find_unique_columns(df):
    print("Columns with unique values:")
    for column in df.columns:
        is_unique = df[column].nunique() == len(df)
        print(f"{column}: {is_unique} (unique values: {df[column].nunique()})")

def import_superfund_sites(file_path):
    df = pd.read_excel(file_path)
    df_lat_lon = pd.read_csv('main/data/superfund/coord.csv')
    
    # Merge the dataframes on EPA ID to get lat and lon
    df = df.merge(df_lat_lon[['EPA ID', 'Latitude', 'Longitude']], 
                 on='EPA ID', 
                 how='left')  # Using left merge to keep all records from main df

    print("Main df shape:", df.shape)
    print("Lat/lon df shape:", df_lat_lon.shape)
    print("Merged df shape:", df.shape)
    print("Sample of merged data:")
    print(df[['EPA ID', 'Latitude', 'Longitude']].head())
    
    # Delete all existing records before importing
    SuperfundSite.objects.all().delete()

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
            rcra_handler_id_name = row['RCRA Handler ID - RCRA Handler Name'],
            lat = row['Latitude'],  # Add the latitude from merged data
            lon = row['Longitude']   # Add the longitude from merged data
            ) for _, row in df.iterrows()]
    
    SuperfundSite.objects.bulk_create(superfund_sites)

class Command(BaseCommand):
    help = 'Import emission event data from Excel file'

    def handle(self, *args, **options):
        superfund_path = 'main/data/superfund/superfund.xlsx'
        emission_path = 'main/data/tecq/tecq.xlsx'

        import_emission_events(emission_path)
        import_superfund_sites(superfund_path)