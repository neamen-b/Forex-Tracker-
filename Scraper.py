from selenium import webdriver
from selenium.webdriver.common.by import By
# imports a tool that allows for the driver to wait for an expected values
from selenium.webdriver.support.ui import WebDriverWait
# has difference expected values parameters
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from typing import Dict, List, Union


class ForexScraper:

    def __init__(self) -> None:
        self.time = time.localtime()
        # Creates an instance of a chrome driver all of the function can use
        # Does not need to create an instance for each function
        self.Chrome_Driver = webdriver.Chrome()

        # Collects the dataframes for each bank
        # Dictionary of {bank name : table data} pairs
        self.bank_tables_dataframe : Dict [str, pd.DataFrame] = {}

        # Holds data from black market website
        # string to str/float pairing
        # Union allows for hinting that a value can be of either type
        # Kind of like set notation, or 'OR' logic
        self.black_market_data : Dict[str , Union [str, float]] = {}

        # merged dataframe with suffxes for every bank
        # Merging on Currency so needs that label initialization
        self.merged_data_frame : pd.DataFrame = pd.DataFrame(columns= ['Currency'])

    
    def Awash (self, URL: str) -> None:
        # Connect to website
        self.Chrome_Driver.get(URL)

        # Wait for page to load
        time.sleep(5)

        # Uses Xpath
        # All tables with given attribute
        # There are several tables on the webpage
        table_element = self.Chrome_Driver.find_element(By.XPATH, './/table[@id = "exchange-rates-table"]')

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
        time.sleep(3)
        #self.Chrome_Driver.quit()

        self.bank_tables_dataframe['Awash'] = df
    
    def CBE (self, URL: str) -> None:
        self.Chrome_Driver.get(URL)

        time.sleep(10)

        # Does not make sure if the table is loaded and has text
        # table = self.Chrome_Driver.find_element(By.TAG_NAME, 'table')
        # CEB site take long to load so making sure the data is there before extracting
        try:
            '''
            WebDriverWait() takes in the driver instance, and wait time before timeput
            until() calls the function provided, webdriverwait, as long as EC is true
            presence checks if the element is present in the DOM
            '''
            table = WebDriverWait(self.Chrome_Driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

        except:
            print('table not found for CBE site')
        
        # Data rows
        table_body = table.find_element(By.TAG_NAME, 'tbody')

        # Each row in body
        tr_in_body = table_body.find_elements(By.TAG_NAME, 'tr')

        # td_in_tr = table_body.find_elements(By.TAG_NAME, 'td')

        rows_text = []
        for row in tr_in_body:
            rows_text.append(row.get_attribute('innerText'))

        all_rows_text = []
        for text in rows_text:
            all_rows_text.append(text.split("\n"))

        attributes = ['Currency','Currency Name', 'Cash Buying', 'Cash Selling', 'Transactional Buying', 'Transactional Selling']
        df = pd.DataFrame(all_rows_text, columns= attributes)

        # print(df)
        # Drop currency name because it is not necessary
        df = df.drop(columns= ['Currency Name'])

        time.sleep(3)
        #self.Chrome_Driver.quit()
        self.bank_tables_dataframe['CBE'] = df
    
    def COOP (self, URL: str) -> None:

        # Connect to website
        self.Chrome_Driver.get(URL)

        # Wait for page to load
        time.sleep(5)

        # Uses Xpath
        # All tables with given attribute
        # There are several tables on the webpage
        table_element = self.Chrome_Driver.find_element(By.XPATH, './/table[@id = "exchange-rates-table"]')

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

        #self.Chrome_Driver.quit()
        
        self.bank_tables_dataframe['COOP'] = df
    
    def Dashen (self, URL: str) -> None:
        # Open browser and access provided URL
        self.Chrome_Driver.get(URL)

        # Sleep to make sure website fully loads
        time.sleep(5)

        # CASH
        # Locate webelement 'table' by tag name
        table_element = self.Chrome_Driver.find_element(By.TAG_NAME, 'table')

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
        transaction_link = self.Chrome_Driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/a')
        transaction_link.click()

        # Make sure webpage loads fully
        time.sleep(5)

        # Exctract data from this table
        # It did not work with Tag name for some reason
        # The table did not have any text when I located it with tag name
        table2_element = self.Chrome_Driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/table')

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
        # This essentially renames all the columns
        merge_df = merge_df[['Currency Code', 'Currency Name', 'Cash Buying', 'Cash Selling', 'Transaction Buying', 'Transaction Selling']]

        # Renaming to make consistent with other banks
        # Key is the old name
        # Values is the new name
        merge_df = merge_df.rename(columns={'Currency Code': 'Currency', 'Transaction Buying' : 'Transactional Buying', 'Transaction Selling' : 'Transactional Selling'})

        # Drop Currency Name column
        # Had issue when merging every bank's table
        merge_df = merge_df.drop(columns=['Currency Name'])
        #self.Chrome_Driver.quit()
        self.bank_tables_dataframe['Dashen'] = merge_df 

    def Hijra (self, URL : str) -> None:
        # Connect to website
        self.Chrome_Driver.get(URL)

        # Wait for page to load
        time.sleep(5)

        # Uses Xpath
        # All tables with given attribute
        # There is only one table on this page
        table_element = self.Chrome_Driver.find_element(By.TAG_NAME, 'table')

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

        # Currency names need to be converted to ISOs
        # Updates columns values to ISOs
        df['Currency'] = ['USD', 'EUR', 'GBP', 'SAR', 'AED']

        # Curreny column has added bits to Currency code. 
        # Needs to be cleaned

        # Currency code has to be fixed
        # For each cell  in column currency, split string on '' and keep on the first part
        # df['Currency'] = df['Currency'].str.split().str[0]
        #print(df)

        #self.Chrome_Driver.quit()
        
        self.bank_tables_dataframe['Hijra'] = df
    
    def NIB (self, URL : str) -> None:
        self.Chrome_Driver.get(URL)

        time.sleep(5)

        # This webpage has two tables
        table_elements = self.Chrome_Driver.find_elements(By.TAG_NAME, 'table')

        # print(table_elements[1].text)
        row_in_table = table_elements[1].find_elements(By.TAG_NAME, 'tr')

        # print(row_in_table[0].get_attribute('outerHTML'))
        table_data = []

        for row in row_in_table:
            row_data = []

            # Finds all immdiate children of each tr element in 'row_in_element' using xpath
            # This makes it more general because tables have header rows data points with tag 'th' instead of 'td'

            data_points = row.find_elements(By.CSS_SELECTOR, 'td, th')

            # The line below does not locate both th and td, instead it returns whichever is True first
            # Something about truthy and falsey
            #data_points = row.find_elements(By.TAG_NAME, 'td' or 'th' )

            # print("Data points", map(lambda x:  x.text in data_points))
            # Testing for content of data_points
            # for data in data_points:
            #     print(data.get_attribute('outerHTML'))
            # print(data_points)
            # go through each data point
            # enumerate is a cool way of enumerating items in a sequence to see where things go wrong.

            for index, data in enumerate(data_points):

                # print(index, data.get_attribute('textContent'))
                # This table has a colmn with images that I do not need. 
                # The image is in an 'img' tag in 'td' tags
                # So this checks if each 'td' or 'th' tag has children i.e, an 'img' tag, and extract only if not
                # if not data.find_element(By.TAG_NAME, './*'):
                # Extract text and add to row data
                # Check if it has text, is so add. Because the first columns in tr are images
                # if data.get_attribute('textContent'):
                row_data.append(data.get_attribute('textContent').strip())
            
            # Add to table data which is a 2D list
            table_data.append(row_data)
        
        # Create DataFrame with 2D array and set columns to first element
        df = pd.DataFrame(table_data, columns= table_data[0])

        # Drop the first row beacause it is the same as the header row
        df = df.drop(labels=0, axis = 0)

        # drop Country column
        # Dropping becuase it is not necessary
        df = df.drop(columns=['Country'])
        # print(table_data,'\n',df)
        self.bank_tables_dataframe['NIB International'] = df    

    def Wegagen (self, URL : str) -> None:
        # Connect to website
        self.Chrome_Driver.get(URL)

        # Wait for page to load
        time.sleep(10)

        table_element = self.Chrome_Driver.find_element(By.TAG_NAME, 'table')

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

        # print(table_data)
        # Create dataframe wtih 2D list
        
        # Initialize list for use as columns in Dataframe
        # Feels like it is not the best solution given it is hard-coding
        columns = ['Image', 'Currency', 'Unit', 'Cash Buying', 'Cash Selling', 'Transactional Buying', 'Transactional Selling']

        df = pd.DataFrame(table_data, columns= columns)

        # I do not need image and unit column
        # Drop by column name
        df = df.drop(columns= ['Image', 'Unit'])

        # self.Chrome_Driver.quit()
        # print(df)
        self.bank_tables_dataframe['Wegagen'] = df

    
    def ETB_Black_Market(self, URL : str) -> None:
        # Connect to website
        self.Chrome_Driver.get(URL)

        # Locate title element by ID
        title = self.Chrome_Driver.find_element(By.ID, 'title')
        # Store text as currency
        self.black_market_data["Currency_ISO"] = title.get_attribute('innerText')

        # Locate the exchange rate element by ID
        exchange_rate = self.Chrome_Driver.find_element(By.ID, 'livePrice')

        # Store rate as float  in dictionary
        # 118.4342 Br
        # Deals with 'Br' by splitting 
        self.black_market_data['Rate'] = float(exchange_rate.get_attribute('innerText').split()[0])


        # Locate the element with date and time
        date_and_time = self.Chrome_Driver.find_element(By.ID, 'date')

        # data is presented in "28/8/2024 - 23:47" format
        # get text and split on hyphen
        date, time = date_and_time.get_attribute('innerText').split('-')

        # Update allows for multiple additions to dictionary at once
        # Takes in a a dictionary of key-value pairs and adds them to existing dict
        self.black_market_data.update({'Date': date , 'Time': time})

    # Merges on Currency* and is an outer join
    # There are disticnt columns for each dataframe
    # Uses tables_dataframe from scrape instance
    def merge_dataframes (self) -> None:

        bank_tables = self.bank_tables_dataframe
        # Create list of banks names and dataframes
        bank_names = list(bank_tables.keys())
        data_frames = list(bank_tables.values())

        # rename each column of the dataframe, except currency, to column name + bank name
        # This is for merging purposes
        # The merged table will have distince column names

        # Enumrate each dataframe
        # Use sequence numver to access banks names 
        for count, frame in enumerate(data_frames):
            
            # Rename each column of current frame to have bank name addes except for the currency column
            # Essentially suffixing before merging
            # Preserve currency becuase merge key is going to be 'Currency'
            # lambda used to apply function to each column name
            frame = frame.rename(columns = lambda x : x + '_' + bank_names[count] if x != 'Currency' else x)

            # print(f'frame after rename')
            # print(frame)
            # Merge currenct frame to aggregate frame on 'Currency'
            self.merged_data_frame = pd.merge(self.merged_data_frame, frame, on = 'Currency', how = 'outer')    

    



