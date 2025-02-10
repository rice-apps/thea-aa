import os
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from ...models import SuperfundSite

class Command(BaseCommand):
    help = "Scrape and update latitude and longitude for SuperfundSite model"

    def handle(self, *args, **kwargs):
        self.update_model_with_lat_long()

    # Set up Selenium WebDriver with Chrome options
    def setup_driver(self):
        service = Service()

        # Set Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode to avoid opening the browser
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        # Initialize the WebDriver
        driver = webdriver.Chrome(service=service, options=options)
        return driver


    # Scrape longitude and latitude for a given epa_id
    def scrape_lat_long(self, driver, epa_id):
        # Construct the EPA URL
        epa_url = f"https://cumulis.epa.gov/supercpad/Cursites/csitinfo.cfm?id={epa_id[-7:]}"
        # print(epa_url)
        driver.get(epa_url)
        time.sleep(3)  # Allow the page to load

        # Try to extract longitude and latitude
        try:
            latitude = driver.find_element(By.XPATH, "//td[normalize-space()='Latitude:']/following-sibling::td").text.strip()
            longitude = driver.find_element(By.XPATH, "//td[normalize-space()='Longitude:']/following-sibling::td").text.strip()

            print(f"EPA ID: {epa_id}, Latitude: {latitude}, Longitude: {longitude}")
            return latitude, longitude
        except Exception as e:
            print(f"Could not extract latitude/longitude for EPA ID {epa_id}: {e}")
            return None, None


    # Update database or file with longitude and latitude
    def update_model_with_lat_long(self):
        # Query all sites that need updates (e.g., missing latitude and longitude)
        sites = SuperfundSite.objects.filter(latitude__isnull=True, longitude__isnull=True)
        # Example data: Replace this with your actual database query or source
        # data = [
        #     {"epa_id": "TXN000606636", "site_name": "A AUTO CRUSHER SALVAGE FIRE"},
        #     # {"epa_id": "TX0000605401", "site_name": "4-AY TRUCKING COMPANY"}
        # ]

        # Set up Selenium driver
        driver = self.setup_driver()

        for site in sites:
            latitude, longitude = self.scrape_lat_long(driver, site.epa_id)
            # latitude, longitude = self.scrape_lat_long(driver, site["epa_id"])
            if latitude and longitude:
                # Update the site model
                site.latitude = latitude
                site.longitude = longitude
                site.save()
                print(f"Updated site {site.epa_id}: Latitude={latitude}, Longitude={longitude}")
            else:
                print(f"No data found for site {site.epa_id}")
            #     print(f"Updated site {site["epa_id"]}: Latitude={latitude}, Longitude={longitude}")
            # else:
            #     print(f"No data found for site {site['epa_id']}")

        # Close the driver
        driver.quit()



