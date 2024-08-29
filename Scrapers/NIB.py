import selenium 
from selenium import webdriver
from selenium.webdriver.common. by import By
import pandas as pd
import time


def get_forex_data (URL: str) -> pd.DataFrame:

    Chrome_Driver = webdriver.Chrome()

    Chrome_Driver.get(URL)

    time.sleep(5)

    # This webpage has two tables
    table_elements = Chrome_Driver.find_elements(By.TAG_NAME, 'table')

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
    
    df = pd.DataFrame(table_data, columns= table_data[0])
    df = df.drop(labels=0, axis = 0)
    print(table_data,'\n',df)


get_forex_data('https://www.nibbanksc.com/exchange-rate/')
         