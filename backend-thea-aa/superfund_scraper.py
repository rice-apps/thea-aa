import os
import glob  # For finding files by pattern
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
from xls2xlsx import XLS2XLSX
import os  


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

# Click the download link to get the Excel file
def download_excel_file(driver):
    try:
        # Locate the download link by its text or href
        download_link = driver.find_element(By.LINK_TEXT, "Download Excel file containing values for all search criteria")
        download_link.click()
        print("Excel file download initiated.")

        # Wait for the download to complete 
        time.sleep(10) 

    except Exception as e:
        print(f"Error downloading the Excel file: {e}")
        
# removed the unnecessary 55 lines and renames the file
def remove_lines_and_rename(download_path):
    print(os.listdir(download_path))

    files = glob.glob(os.path.join(download_path, 'cqry*.xls')) # Downloaded file
    old_name = files[0]  # Assume there's only one matching file
    filename, ext = os.path.splitext(os.path.basename(old_name))
    new_name = filename[:4] + ext
    print(" Created " + new_name)
    new_path = os.path.join(download_path, new_name)

    with open(old_name, "r") as file:
        lines = file.readlines()

    with open(new_path, "w") as file:
        for line in lines[54:]:
            file.write(line)

    os.remove(old_name)

# Scrape latitude and longitude
def scrape_lat_long(driver, epa_id):
    epa_url = f"https://cumulis.epa.gov/supercpad/Cursites/csitinfo.cfm?id={epa_id[-7:]}"
    driver.get(epa_url)
    time.sleep(3)

    try:
        latitude = driver.find_element(By.XPATH, "//td[normalize-space()='Latitude:']/following-sibling::td").text.strip()
        longitude = driver.find_element(By.XPATH, "//td[normalize-space()='Longitude:']/following-sibling::td").text.strip()
        print(f"EPA ID: {epa_id}, Latitude: {latitude}, Longitude: {longitude}")
        return latitude, longitude
    except Exception as e:
        print(f"Could not extract latitude/longitude for EPA ID {epa_id}: {e}")
        return None, None

# Update CSV with Latitude and Longitude
def update_csv_with_lat_long(download_path):
    csv_file_path = os.path.join(download_path, "superfund.csv")
    df = pd.read_csv(csv_file_path)

    # Ensure EPA ID column exists
    if 'EPA ID' not in df.columns:
        print("EPA ID column not found.")
        return
    
    # Add latitude and longitude columns if not exist
    if 'Latitude' not in df.columns:
        df['Latitude'] = None
    if 'Longitude' not in df.columns:
        df['Longitude'] = None

    driver = setup_driver(download_path)

    # Perform scraping for missing data
    for index, row in df.iterrows():
        if pd.isnull(row['Latitude']) or pd.isnull(row['Longitude']):
            latitude, longitude = scrape_lat_long(driver, row['EPA ID'])
            if latitude and longitude:
                df.at[index, 'Latitude'] = latitude
                df.at[index, 'Longitude'] = longitude
                print(f"Updated EPA ID {row['EPA ID']} with Latitude: {latitude}, Longitude: {longitude}")
            else:
                print(f"No data found for EPA ID {row['EPA ID']}")

    driver.quit()

    # Save updated CSV
    df.to_csv(csv_file_path, index=False)
    print("Updated CSV with latitude and longitude data.")

def convert_to_csv(downloaded_path):
    # downloaded_path will be: /thea-aa/backend-thea-aa/downloads
    
    # relative paths to the stored .xls file
    xls_file_path = downloaded_path + "/cqry.xls"
    print("xls saved file path: ",xls_file_path)
    xlsx_file_path = "main/data/superfund/superfund.xlsx"

    # convert to xlxs
    converter = XLS2XLSX(xls_file_path)
    clean_download_folder(downloaded_path)
    converter.to_xlsx(xlsx_file_path)
    print("\nConverted the .xls to .xlxs file\n")
    
    # # Convert XLSX to CSV using pandas
    # csv_file_path = os.path.join(downloaded_path, "superfund.csv")
    # try:
    #     df = pd.read_excel(xlsx_file_path)
    #     df.to_csv(csv_file_path, index=False)
    #     print("Saved CSV file successfully.")
    # except Exception as e:
    #     print(f"Error during CSV conversion: {e}")
    # read the data
    df = pd.read_excel(xlsx_file_path)
    print("Read the .xlxs file as Pandas DataFrame\n")
    
    # delete converted folder files
    print("Clear the data/superfund folder")
    clean_download_folder(downloaded_path)
    
    # then save the csv file back to the converted
    os.makedirs('main/data/superfund/', exist_ok=True)  
    df.to_csv('main/data/superfund/superfund.csv')  
    print("Saved the Superfund data as csv successfully!")
     
    
def main():
     # Set the download path relative to the project directory
    download_path = os.path.join(os.getcwd(), "main/data/superfund")
    os.makedirs(download_path, exist_ok=True)

    # Clean the download folder before downloading a new file
    clean_download_folder(download_path)

    driver = setup_driver(download_path)
    search_for_state(driver)

    # Initiate the file download
    download_excel_file(driver)

    # Close the browser
    driver.quit()
    print(f"Excel file saved to: {download_path}")

    remove_lines_and_rename(download_path)
    
    convert_to_csv(download_path)

    # Update with lat/long data
    update_csv_with_lat_long(download_path)

if __name__ == "__main__":
    main()
