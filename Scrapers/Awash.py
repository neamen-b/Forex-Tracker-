import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from typing import Dict


def get_forex_data(URL: str) -> Dict [str, pd.DataFrame]:

    # Instance of a chrome driver
    Chrome_Driver = webdriver.Chrome()

    # Connect to website
    Chrome_Driver.get(URL)

    # Wait for page to load
    time.sleep(5)

    # Uses Xpath
    # All tables with given attribute
    # There are several tables on the webpage
    table_element = Chrome_Driver.find_element(By.XPATH, './/table[@id = "exchange-rates-table"]')

    # header part has two rows
    # first has 3 (Currency, Cash, Transaction) and second has 4 ( Cash: [Buying, Seeling], Transaction: [Buying, Selling])
    #  way to fix this
    #   1. Just create your own header row and extract text in body (Easier)
    # Only reading rows in table body to avoid issue with complex header rows
    rows_in_table_body = table_element.find_elements(By.XPATH, './/tbody/tr')

    # 2D list to store data of table
    table_data = []

    # Go through each row
    for row in rows_in_table_body:
        # Stores data for each row and is added to table_data
        row_data = []

        # Locate all td elements in row
        data_points_in_row = row.find_elements(By.XPATH, './/td')

        # Appends each data point in row
        for data_point in data_points_in_row:
            row_data.append(data_point.get_attribute('innerText'))
        
        # Add row data to table data
        table_data.append(row_data)


    # Create dataframe wtih 2D list
    
    # Initialize list for use as columns in Dataframe
    # Feels like it is not the best solution given it is hard-coding
    columns = ['Currency', 'Cash Buying', 'Cash Selling', 'Transactional Buying', 'Transactional Selling']

    df = pd.DataFrame(table_data, columns= columns)

    # Curreny column has added bits to Currency code. 
    # Needs to be cleaned

    # For each cell  in column currency, split string on '' and keep on the first part
    df['Currency'] = df['Currency'].str.split().str[0]
    #print(df)

    Chrome_Driver.quit()

    return {'Awash' : df}

print(get_forex_data('https://awashbank.com/exchange-historical/'))

    

