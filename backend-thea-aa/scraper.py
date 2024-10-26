import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import xlsxwriter
from selenium.webdriver.support.ui import Select


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

def main():
     # Set the download path relative to the project directory
    download_path = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_path, exist_ok=True)

    driver = setup_driver(download_path)
    search_for_state(driver)

    # Initiate the file download
    download_excel_file(driver)

    # Close the browser
    driver.quit()
    print(f"Excel file saved to: {download_path}")


if __name__ == "__main__":
    main()
