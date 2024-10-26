import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import xlsxwriter
from selenium.webdriver.support.ui import Select


# Set up Selenium WebDriver with Chrome options
def setup_driver(download_path):
    service = Service()  # Make sure chromedriver is in PATH

    # Set Chrome options for downloading files
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path,  # Set your download path
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

        # Wait for the download to complete (adjust timeout if necessary)
        time.sleep(10)  # Ensure download completes before proceeding

    except Exception as e:
        print(f"Error downloading the Excel file: {e}")

# # extract event urls
# def extract_event_urls(driver):
#     # Wait until the table rows are present in the HTML structure
#     try:
#         table = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.TAG_NAME, 'table'))
#         )
#     except Exception as e:
#         print(f"Table not found: {e}")
#         return []

#     # Now locate the <tr> elements inside the table
#     rows = table.find_elements(By.TAG_NAME, 'tr')
#     event_urls = []
#     # Locate all <tr> elements in the table that contain event data
#     rows = driver.find_elements(By.TAG_NAME, 'tr')
#     print(rows)
    
#     event_urls = []
    
#     # Loop through each row to find the <a> tags with event links
#     for row in rows:
#         try:
#             # Find the <a> element within the row
#             link_element = row.find_element(By.TAG_NAME, 'a')
#             href = link_element.get_attribute('href')  # Get the href attribute
            
#             # Append the full URL (base + href) to event_urls
#             full_url = f"https://cumulis.epa.gov/supercpad/Cursites/{href}"
#             event_urls.append(full_url)
        
#         except Exception as e:
#             print(f"Error processing row: {e}")
    
#     return event_urls

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

    # # Collect event IDs
    # event_urls = extract_event_urls(driver)
    # print(f"Found {len(event_urls)} events")
    # print(event_urls)

    # # Scrape data for each event
    # all_data = []
    # for event_id in event_ids:
    #     try:
    #         event_data = scrape_event_details(driver, event_id)
    #         all_data.append(event_data)
    #     except Exception as e:
    #         print(f"Error scraping event {event_id}: {e}")

    # # Save all data to Excel
    # save_to_excel(all_data)
    # print("Scraping completed and data saved to Excel.")

    # # Close the browser
    # driver.quit()

if __name__ == "__main__":
    main()
# import pandas as pd

# # Replace 'your_file.xlsx' with the path to your Excel file
# df = pd.read_excel('./superfund.xlsx')

# # Display the first few rows
# print(df.head())