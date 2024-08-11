import selenium 
from selenium import webdriver
from selenium.webdriver.common. by import By
import pandas as pd
import time


# Function accesses Dashen's Forex webpage and extracts tabular data
def get_table_data (URL :str) -> pd.DataFrame:
    # Create an instance of the webdriver
    Chrome_Driver = webdriver.Chrome()

    # Open browser and access provided URL
    Chrome_Driver.get(URL)

    # Sleep to make sure website fully loads
    time.sleep(5)

    # CASH
    # Locate webelement 'table' by tag name
    table_element = Chrome_Driver.find_element(By.TAG_NAME, 'table')

    # Locate rows in 'table'
    # returns a list of webelement corresponding to each row
    table_rows = table_element.find_elements(By.TAG_NAME, 'tr')
    
    # 2D list to collect data from every row
    table_data = []

    # access each row in table rows
    for row in table_rows:
        # define list to store data of each row
        row_data = []

        # Locate webelements that contain data at each column
        td = row.find_elements(By.TAG_NAME, 'td')

        # access data at each column for this row and add to row data
        for data in td:
            row_data.append(data.text)
        
        # Add row data to table data. Creating a list of lists
        table_data.append(row_data)

        # Troubleshooting
        # print('Row Data point', data.text)
        # print('table data', table_data)
        # print(row.text)
        # row_data.append(row.text.split())
    
    # TRANSACTION
    # Locate the transaction table link and click it
    transaction_link = Chrome_Driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/a')
    transaction_link.click()

    # Make sure webpage loads fully
    time.sleep(5)

    # Exctract data from this table
    # It did not work with Tag name for some reason
    # The table did not have any text when I located it with tag name
    table2_element = Chrome_Driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/table')


    # Locate rows in 'table'
    # returns a list of webelement corresponding to each row
    table2_rows = table2_element.find_elements(By.TAG_NAME, 'tr')
    
    # 2D list to collect data from every row
    table2_data = []

    # access each row in table rows
    for row in table2_rows:
        # define list to store data of each row
        row_data = []

        # Locate webelements that contain data at each column
        td = row.find_elements(By.TAG_NAME, 'td')

        # access data at each column for this row and add to row data
        for data in td:
            row_data.append(data.text)
        
        # Add row data to table data. Creating a list of lists
        table2_data.append(row_data)

    # Create a dataframe with the 2D list
    # I want to create the data frames with the first element in the 2D list as the columns
    # This uses list splicing and indexing to accomplish that
    # Create DataFrame starting from index 0 and set columns as the first element
    df = pd.DataFrame(table_data[1:], columns= table_data[0])
    df2 = pd.DataFrame(table2_data[1:], columns= table2_data[0])




    # Merges the two daraframes on Currency Code
    # Now the table includes both CASH and Transactional
    # The Curreny Name for df2 got dropped to avoid repetitive columns but that means
    # that the ONLY TRANSACTION currencies don't have a name
    # Needs to get fixes but good enough for now

    # merge_df = pd.merge(df, df2.drop(columns= ['Currency Name']), on= 'Currency Code', how= 'outer')

    # Solution to previous merge problem
    # Just merge first
    merge_df = pd.merge(df, df2, on='Currency Code', how='outer')

    # There will be two Currency name columns, but they can be combined and later dropped
    # This combines the two columns. Sources data from the first columns, If NAN, then sources from df2
    merge_df['Currency Name'] = merge_df['Currency Name_x'].combine_first(merge_df['Currency Name_y'])

    # Dropping the original two columns
    merge_df = merge_df.drop(columns=['Currency Name_x', 'Currency Name_y'])

    # Rearrange columns because 'Currency Name' was addess to the end
    merge_df = merge_df[['Currency Code', 'Currency Name', 'Cash Buying', 'Cash Selling', 'Transaction Buying', 'Transaction Selling']]

    print(merge_df)
    Chrome_Driver.quit()
    
    return merge_df

    # Troubleshooting
    # merge = pd.concat([df, df2], axis = 1)
    # print(merge_df)
    # print("table2",data.text)
    # row_data.pop(0)
    # print("Row Data \n", row_data)
    # df.to_csv(r'C:\Users\Neamen\Desktop\Dashen.csv')
    # print(df)
    # print(f"table 2 text{table2_element.text}")
    # print("df1",df)
    # print("df2", df2)
        
get_table_data("https://dashenbanksc.com/daily-exchange-rates-2/")


