import os
import glob  # For finding files by pattern
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
from xls2xlsx import XLS2XLSX
import pandas as pd  


# Set up Selenium WebDriver with Chrome options
def setup_driver(download_path):
    service = Service()

    # Set Chrome options for downloading files
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path,  # Set download path
        "download.prompt_for_download": False,  # Avoid download confirmation
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True  # Disable warnings
    }
    options.add_experimental_option("prefs", prefs)

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Clean old files from the download directory
def clean_download_folder(download_path):
    files = glob.glob(os.path.join(download_path, '*'))  # Get all files in the folder
    for f in files:
        try:
            os.remove(f)  # Delete each file
            print(f"Deleted old file: {f}")
        except Exception as e:
            print(f"Error deleting file {f}: {e}")

# Navigate to the search page and perform a search for Texas (TX)
def search_for_state(driver):
    # Load the search form page
    search_url = "https://cumulis.epa.gov/supercpad/Cursites/srchsites.cfm"
    driver.get(search_url)
    time.sleep(3)  # Allow the page to load

    # Select the state "TX" from the dropdown
    state_dropdown = Select(driver.find_element(By.ID, "state"))
    state_dropdown.select_by_value("TX")  # Select Texas

    # Locate and click the search button using its ID
    search_button = driver.find_element(By.ID, 'submit1')
    search_button.click()

def extract_records_with_long_lat(driver):
    """
    Extract records from the table, including latitude and longitude.
    """
    records = []

    # Locate the table by ID
    table = driver.find_element(By.ID, "tablesorter")
    rows = table.find_elements(By.XPATH, ".//tbody/tr")  # Get all rows in the table body
    print(len(rows))
    
    for i in range(len(rows)):
        row = rows[i]
        try:
            # Extract data from columns
            epa_id = row.find_element(By.XPATH, "./td[1]").text
            site_name = row.find_element(By.XPATH, "./td[2]").text
            city = row.find_element(By.XPATH, "./td[3]").text
            county = row.find_element(By.XPATH, "./td[4]").text
            state = row.find_element(By.XPATH, "./td[5]").text
            national_priority_list_status = row.find_element(By.XPATH, "./td[6]").text
            superfund_alternative_approach = row.find_element(By.XPATH, "./td[7]").text
            construction_complete = row.find_element(By.XPATH, "./td[8]").text
            sitewide_ready_for_anticipated_use = row.find_element(By.XPATH, "./td[9]").text
            human_exposure_under_control = row.find_element(By.XPATH, "./td[10]").text
            groundwater_migration_under_control = row.find_element(By.XPATH, "./td[11]").text

            # Get the link to the individual page
            site_link = row.find_element(By.XPATH, "./td[2]/a").get_attribute("href")

            # Navigate to the individual page and extract latitude and longitude
            latitude, longitude = extract_lat_long_from_record(driver, site_link)

            # Append data to records
            records.append({
                "EPA ID": epa_id,
                "Site Name": site_name,
                "City": city,
                "County": county,
                "State": state,
                "National Priority List Status": national_priority_list_status,
                "Superfund Alternative Approach": superfund_alternative_approach,
                "Construction Complete": construction_complete,
                "Sitewide Ready for Anticipated Use": sitewide_ready_for_anticipated_use,
                "Human Exposure Under Control": human_exposure_under_control,
                "Groundwater Migration Under Control": groundwater_migration_under_control,
                "Latitude": latitude,
                "Longitude": longitude,
            })

        except Exception as e:
            print(f"Error processing table {i}: {e}")
        
    return records

def extract_lat_long_from_record(driver, record_url):
    """
    Extract latitude and longitude from an individual record's page.
    """
    driver.get(record_url)
    time.sleep(2)  # Wait for the page to load

    try:
        # Locate the table containing latitude and longitude
        table = driver.find_element(By.CLASS_NAME, "nostyle")
        
        latitude = None
        longitude = None
        
        # Extract latitude and longitude using their labels
        try:
            latitude = table.find_element(By.XPATH, ".//td[strong[contains(text(), 'Latitude')]]/following-sibling::td").text.strip()
        except Exception:
            print(f"Latitude not found for {record_url}. Adding NaN.")

        try:
            longitude = table.find_element(By.XPATH, ".//td[strong[contains(text(), 'Longitude')]]/following-sibling::td").text.strip()
        except Exception:
            print(f"Longitude not found for {record_url}. Adding NaN.")

        return latitude, longitude
    except Exception as e:
        print(f"Error extracting latitude/longitude from {record_url}: {e}")
        return None, None
    
def main():
     # Set the download path relative to the project directory
    download_path = os.path.join(os.getcwd(), "backend-thea-aa/downloads")
    os.makedirs(download_path, exist_ok=True)

    # Clean the download folder before downloading a new file
    clean_download_folder(download_path)

    driver = setup_driver(download_path)
    search_for_state(driver)
    
    records = extract_records_with_long_lat(driver)
    print("Extracted records with coordinates:")
    
    # Save the extracted records to a CSV file
    df = pd.DataFrame(records)
    output_file = os.path.join(download_path, "superfund_data.csv")
    df.to_csv(output_file, index=False)
    print(f"Saved extracted records with coordinates to {output_file}")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
