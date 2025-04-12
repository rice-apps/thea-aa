from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import xlsxwriter
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

global switch
global case_tracker
global counter
global last_count
global single_incident
global single_case


def number_finder(text):
    return any(i.isdigit() for i in text)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def new_line_remover(question):
    if '\n' in question.__getattribute__('text'):
        return question.__getattribute__('text').replace('\n', '')
    else:
        return question.__getattribute__('text')


def setup():
    global single_case
    global single_incident

    # Configure Chrome options for GitHub Actions environment
    options = Options()
    # options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
    options.binary_location = '/opt/hostedtoolcache/setup-chrome/chromium/135.0.7049.52/x64/chrome'
    service = Service('/opt/hostedtoolcache/setup-chrome/chromedriver/135.0.7049.52/x64/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    # Go to Website.
    driver.get('https://www2.tceq.texas.gov/oce/eer/index.cfm')

    # Find input boxes
    print('Enter Incident Number:')
    single_search = input()
    if len(single_search) > 0:
        incident_number = driver.find_element(By.NAME, 'incid_track_num')
        incident_number.send_keys(single_search)
        single_case = True
        single_incident = [single_search]
    else:
        single_case = False
        event_start_beg = driver.find_element(By.NAME, 'event_start_beg_dt')
        event_start_end = driver.find_element(By.NAME, 'event_start_end_dt')
        event_end_beg = driver.find_element(By.NAME, 'event_end_beg_dt')
        event_end_end = driver.find_element(By.NAME, 'event_end_end_dt')
        cn = driver.find_element(By.NAME,  'cn_txt')
        customer_name = driver.find_element(By.NAME, 'cust_name')
        rn = driver.find_element(By.NAME, 'rn_txt')
        regulated_entity_name = driver.find_element(By.NAME, 're_name')
        county = driver.find_element(By.NAME, 'ls_cnty_name')
        region = driver.find_element(By.NAME, 'ls_region_cd')
        event_type = driver.find_element(By.NAME, 'ls_event_typ_cd')

        #Best Test Date 2/14/2021
        print('Enter Beginning Start Date Range (##/##/####):')
        beginning_start = input()
        event_start_beg.send_keys(beginning_start)
        print('Enter Last Start Date Range (##/##/####):')
        last_start = input()
        event_start_end.send_keys(last_start)
        print('Enter Beginning End Date Range (##/##/#### must be after 1/31/2003):')
        end_start = input()
        event_end_beg.send_keys(end_start)
        print('Enter Last End Date Range (##/##/#### must be after 1/31/2003):')
        end_end = input()
        event_end_end.send_keys(end_end)
        print('Enter CN:')
        cn_input = input()
        cn.send_keys(cn_input)
        print('Enter Customer Name:')
        customer_name_input = input()
        customer_name.send_keys(customer_name_input)
        print('Enter RN:')
        rn_input = input()
        rn.send_keys(rn_input)
        print('Enter Regulated Entity Name:')
        regulated_entity_name_input = input()
        regulated_entity_name.send_keys(regulated_entity_name_input)
        print('Enter County:')
        county_input = input()
        county.send_keys(county_input)
        print('Enter Region (REGION ## - _____):')
        region_input = input()
        region.send_keys(region_input)
        print('Enter Event Type:')
        event_type_input = input()
        event_type.send_keys(event_type_input)

    # Click submit
    search = driver.find_element(By.NAME, '_fuseaction=main.searchresults')
    search.click()
    print('Processing Now...')

    return driver


def collecting_information(driver):
    cases = []
    case_numbers = []
    repeat = True

    while repeat:
        # Wait until the data display elements are present
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'datadisplay'))
        )
        
        for lines in link:
            case = lines.find_elements(By.TAG_NAME, 'a')
            for sublinks in case:
                if number_finder(sublinks.get_attribute('text')):
                    cases.append(sublinks.get_attribute('href'))
                    case_numbers.append(sublinks.get_attribute('text'))

        # Wait until the paging navigation elements are present
        navigation = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'pagingnav'))
        )
        navigation_links = navigation[0].find_elements(By.CSS_SELECTOR, 'a') if navigation else []

        next_impossible = True
        for pages in navigation_links:
            if pages.text == '>':
                driver.get(pages.get_attribute('href'))
                next_impossible = False
                break

        if next_impossible:
            repeat = False

    return cases



def time_converter(half, time):
    sep = time.split(":")
    hour = int(sep[0])
    if (hour == 12):
        hour = 0
    if (half == 'PM'):
        hour += 12
    return str(hour) + ':' + str(sep[1])


def filling_sheet(sheet, sheet2, number, cell0, cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8,
                  cell9, cell10, cell19, cell20, cell21, cell22, cell23):
    i = last_count
    global counter
    if switch:
        i += 1
    #330891 is Kaiba's test case
    if counter == 1:
        counter = 2
    while i < counter:
        #incident number
        sheet.write_url(i, 0, cell0, string=number)
        #RN number
        sheet.write(i, 1, cell1)
        #RE Name
        sheet.write(i, 2, cell2)
        #Physical Location
        sheet.write(i, 3, cell3)
        #County
        sheet.write(i, 4, cell4)
        #TCEQ Region
        sheet.write(i, 5, cell5)
        #Start Date/Time
        sheet.write(i, 6, cell6)
        #End Date/Time
        sheet.write(i, 7, cell7)
        #Event Type
        sheet.write(i, 8, cell8)
        #Emission Point Name
        sheet.write(i, 9, cell9)
        #EPN
        sheet.write(i, 10, cell10)
        #Cause of Emission Event
        sheet.write(i, 20, cell20)
        #Actions Taken
        sheet.write(i, 21, cell21)
        #Basis Used
        sheet.write(i, 22, cell19)
        #Report Type
        #sheet.write(i, 22, cell22)
        #Initial Notification
        sheet.write(i, 23, cell23)
        #Hours Elapsed
        sheet.write(i, 24, '=(H' + str(i+1) + '-G' + str(i+1) + ')*24')
        #Emissions Rate (lbs/hr)
        sheet.write(i, 25, '=M' + str(i+1) + '/Y' + str(i+1))
        #Flag
        sheet.write(i, 26, '=IF(Z' + str(i+1) + '>=Q' + str(i+1) + ',"Y","N")')
        i += 1
    global case_tracker
    sheet2.write_url(case_tracker - 1, 0, cell0, string=number)
    #sheet2.write(case_tracker - 1, 1, "=SUMIF(Cases!A:A,'Incident Sums'!A" + str(case_tracker) + ",Cases!M:M)")
    #SUMIF(Cases!A: A, 'Incident Sums'!A" + str(case_tracker) + ", Cases!M: M)
    #=SUMIFS(Cases!M:M,Cases!A:A,'Incident Sums'!A2,Cases!P:P,"<>*OPACITY*")
    sheet2.write(case_tracker - 1, 1, "=SUMIFS(Cases!M:M,Cases!A:A,'Incident Sums'!A" + str(case_tracker) + ',Cases!P:P,"<>*OPACITY*")')
    case_tracker += 1


def contaminants(questions, answers, order, sheet, sheet2, j):
    # Loop Counters
    questions_counter = 0
    answers_counter = 0
    number_of_contaminants = 0
    global switch
    global counter
    global last_count

    # Gathering Information
    while questions_counter < len(questions):
        print_out = new_line_remover(questions[questions_counter])
        if 'List of Air Contaminant Compounds' in questions[questions_counter].__getattribute__('text'):
            splitting = questions[questions_counter].__getattribute__('text').split()
            for s in splitting:
                if s.isnumeric():
                    number_of_contaminants = int(s)
            questions_counter += 1
        else:
            if number_of_contaminants > 0:
                questions_counter += 6

                while number_of_contaminants > 0:
                    contaminant = (answers[answers_counter].__getattribute__('text'))
                    sheet.write(counter, 11, contaminant)
                    answers_counter += 1

                    quantity = answers[answers_counter].__getattribute__('text')
                    #while True:
                        #try:
                    if isfloat(quantity):
                        sheet.write(counter, 12, float(quantity))
                    else:
                        sheet.write(counter, 12, quantity)
                            #break
                        #except ValueError:
                            #sheet.write(counter, 12, quantity)
                            #break

                    answers_counter += 1

                    unit_measurement = answers[answers_counter].__getattribute__('text')
                    sheet.write(counter, 15, unit_measurement)
                    answers_counter += 1

                    emissionlimit = answers[answers_counter].__getattribute__('text')
                    sheet.write(counter, 16, float(emissionlimit))
                    answers_counter += 1

                    units = answers[answers_counter].__getattribute__('text')
                    sheet.write(counter, 17, units)
                    answers_counter += 1

                    authorization = answers[answers_counter].__getattribute__('text')
                    sheet.write(counter, 18, authorization)
                    answers_counter += 1

                    counter += 1

                    number_of_contaminants -= 1
            else:
                count = True
                answer = answers[answers_counter].__getattribute__('text')
                #print(print_out)
                #print('answer[' + str(answers_counter) + '] '+ answer)
                if print_out == 'Incident Tracking Number:':
                    number = answer
                    cell0 = j
                elif print_out == 'RN:':
                    cell1 = answer
                elif print_out == 'Regulated Entity Name:':
                    cell2 = answer
                elif print_out == 'Physical Location:':
                    cell3 = answer
                elif print_out == 'County:':
                    cell4 = answer
                #bookmark
                elif print_out == 'Notification Jurisdictions:':
                    x = answer.split(" ")
                    if len(x) > 1:
                        cell5 = int(x[1])
                    else:
                        cell5 = " "
                elif print_out == 'Process Unit or Area Common Names':
                    text = order[2].__getattribute__('text').split("\n")
                    answers_counter += (len(text) - 1)
                    questions_counter += 1
                    count = False
                elif print_out == 'Facility Common Name':
                    text = order[3].__getattribute__('text').split("\n")
                    answers_counter += (len(text) - 1) * 2
                    questions_counter += 2
                    count = False
                elif print_out == 'Date and Time Event Discovered or Scheduled Activity Start:':
                    y = answer.split(" ")
                    time1 = time_converter(y[-1], y[-2])
                    cell6 = str(y[0]) + ' ' + time1
                elif print_out == 'Date and Time Event or Scheduled Activity Ended:':
                    z = answer.split(" ")
                    if len(z) > 1:
                        time2 = time_converter(z[-1], z[-2])
                    else:
                        time2 = z[0]
                    cell7 = str(z[0]) + ' ' + time2
                elif print_out == 'Event/Activity Type:':
                    cell8 = answer
                elif print_out == '1 - Emission Point Common Name:':
                    cell9 = answer
                elif print_out == 'Emission Point Common Name:':
                    cell9 = 'N/A'
                elif print_out == 'Emission Point Number:':
                    cell10 = answer
                elif print_out == 'Basis Used to Determine Quantities and Any Additional Information Necessary to Evaluate the Event:':
                    cell19 = answer
                elif print_out == 'Cause of Emission Event or Excess Opacity Event, or Reason for Scheduled Activity:':
                    cell20 = answer
                elif print_out == 'Actions Taken, or Being Taken, to Minimize Emissions And/or Correct the Situation:':
                    cell21 = answer
                elif print_out == 'Report Type:':
                    cell22 = answer
                elif print_out == 'Initial Notification Date/Time:':
                    cell23 = answer
                if count:
                    questions_counter += 1
                    answers_counter += 1
    filling_sheet(sheet, sheet2, number, cell0, cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8,
                  cell9, cell10, cell19, cell20, cell21, cell22, cell23)
    if switch:
        switch = False
    last_count = counter


def extracting_information(driver, cases):
    direct = os.getcwd() + '/TCEQ_Data.xlsx'
    book = xlsxwriter.Workbook(direct)
    sheet = book.add_worksheet('Cases')
    sheet2 = book.add_worksheet('Incident Sums')
    global case_tracker
    case_tracker = 2
    download = driver.find_element(By.ID, 'dwnldlink')
    download.click()
    # sheet.set_column(0, 1, 100)
    sheet.write(0, 0, 'INCIDENT NO.')
    sheet.write(0, 1, 'RN')
    sheet.write(0, 2, 'RE NAME')
    sheet.write(0, 3, 'PHYSICAL LOCATION')
    sheet.write(0, 4, 'COUNTY')
    sheet.write(0, 5, 'TCEQ REGION')
    sheet.write(0, 6, 'START DATE/TIME')
    sheet.write(0, 7, 'END DATE/TIME')
    sheet.write(0, 8, 'EVENT TYPE')
    sheet.write(0, 9, 'EMISSION POINT NAME')
    sheet.write(0, 10, 'EPN')
    sheet.write(0, 11, 'CONTAMINANT')
    sheet.write(0, 12, 'EST QUANTITY/OPACITY')
    sheet.write(0, 13, 'ESTIMATED IND')
    sheet.write(0, 14, 'AMOUNT UNK IND')
    sheet.write(0, 15, 'UNITS')
    sheet.write(0, 16, 'EMISSION LIMIT')
    sheet.write(0, 17, 'LIMIT UNITS')
    sheet.write(0, 18, 'AUTHORIZATION COMMENT')
    sheet.write(0, 19, 'COMMENT NO')
    sheet.write(0, 20, 'Cause of Emission Event')
    sheet.write(0, 21, 'Actions Taken')
    sheet.write(0, 22, 'Basis Used to Determine Quantities and Any Additional Information Necessary to Evaluate the Event')
    #sheet.write(0, 22, 'Report Type:')
    sheet.write(0, 23, 'Initial Notification:')
    sheet.write(0, 24, 'Hours Elapsed:')
    sheet.write(0, 25, 'Emissions Rate (lbs/hr):')
    sheet.write(0, 26, 'Flag(Y/N):')

    sheet2.write(0, 0, 'INCIDENT NO.')
    sheet2.write(0, 1, 'INCIDENT SUM(POUNDS)')

    global counter
    global last_count
    global switch
    global single_incident
    global single_case

    counter = 0
    last_count = 0
    switch = True
    # Clicking through the files
    if single_case == False:
        count = True
        for j in cases:
            if (count):
                counter += 1
                count = False
            # Go to files
            driver.get(j)
            # Yellow Boxes
            questions = driver.find_elements(By.TAG_NAME, 'th')
            # White Boxes
            answers = driver.find_elements(By.TAG_NAME, 'td')
            # Seperated by forms
            order = driver.find_elements(By.CLASS_NAME, 'aeme')

            contaminants(questions, answers, order, sheet, sheet2, j)
    else:
        counter += 1
        j = driver.current_url

        # Yellow Boxes
        questions = driver.find_elements(By.TAG_NAME, 'th')
        # White Boxes
        answers = driver.find_elements(By.TAG_NAME, 'td')
        # Seperated by forms
        order = driver.find_elements(By.CLASS_NAME, 'aeme')

        contaminants(questions, answers, order, sheet, sheet2, j)
    book.close()


def main():
    global single_case
    global single_incident
    driver = setup()
    if single_case:
        extracting_information(driver, single_incident)
    else:
        cases = collecting_information(driver)
        extracting_information(driver, cases)
    driver.quit()
    
main()
