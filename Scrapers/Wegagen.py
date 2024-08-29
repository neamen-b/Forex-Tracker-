import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


def get_forex_data(URL: str) -> pd.DataFrame:

    # Instance of a chrome driver
    Chrome_Driver = webdriver.Chrome()

    # Connect to website
    Chrome_Driver.get(URL)

    # Wait for page to load
    time.sleep(5)


    table_element = Chrome_Driver.find_element(By.TAG_NAME, 'table')

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

    print(table_data)
    # Create dataframe wtih 2D list
    
    # Initialize list for use as columns in Dataframe
    # Feels like it is not the best solution given it is hard-coding
    columns = ['Image', 'Currency', 'Unit', 'Cash Buying', 'Cash Selling', 'Transactional Buying', 'Transactional Selling']

    df = pd.DataFrame(table_data, columns= columns)

    # I do not need image and nuit column
    df = df.drop(columns= ['Image', 'Unit'])

    Chrome_Driver.quit()
    print(df)
    return df

get_forex_data('https://wegagen.com/')

    

