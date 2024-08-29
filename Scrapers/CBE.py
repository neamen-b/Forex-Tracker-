from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

import pandas
from selenium.webdriver.common.by import By


def get_forex_data(URL: str) -> pandas.DataFrame:

    # Chrome_Driver = webdriver.Chrome()
    #URL = "https://www.combanketh.et/en/exchange-rate/"
    # Chrome_Driver.get(URL)


    Chrome_Driver = webdriver.Chrome()

    Chrome_Driver.get(URL)

    time.sleep(5)

    table = Chrome_Driver.find_element(By.TAG_NAME, 'table')

    # print(table.text)

    # # Header row
    # th = table.find_elements(By.TAG_NAME,'th')

    # attributes = ['Ticker']
    # for line in th:
    #     # print("-----------")
    #     attributes.append(line.text)
    #     # print(line.text)

    # Data rows
    table_body = table.find_element(By.TAG_NAME, 'tbody')

    tr_in_body = table_body.find_elements(By.TAG_NAME, 'tr')

    # td_in_tr = table_body.find_elements(By.TAG_NAME, 'td')

    rows = []
    for row in tr_in_body:
        rows.append(row.text)



    all_rows = []
    for row in rows:
        all_rows.append(row.split("\n"))

    attributes = ['Currency','Currency Name', 'Cash Buying', 'Cash Selling', 'Transactional Buying', 'Transactional Selling']
    df = pandas.DataFrame(all_rows, columns= attributes)

    # print(df)

    # time.sleep(3)
    Chrome_Driver.quit()
    return df
    # df.to_csv(path_or_buf= r'C:\Users\Neamen\Desktop\CBE_Forex_08_08_2024.csv', index= False)

print(get_forex_data("https://www.combanketh.et/en/exchange-rate/"))


# columns = soup.find_all('th')

# print(columns)

# attributes = [attribute.text.strip() for attribute in columns]
# print(attributes)

# rows = soup.find_all('tbody', recursive= True)
# print(rows)

# soup = BeautifulSoup(html, 'html.parser')

# text = soup.getText("\n")

# print(text)

# data = []
# for td in td_in_tr:
#     print("-----------")
#     data.append(td.text)
#     print(td.text)


# print(attributes)
# print(data)
# print(rows)
# table_soup = BeautifulSoup(table.get_attribute('outerHTML'), 'html.parser')
# table_soup.find_all('th')
# web_page = Chrome_Driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/div/div/div/div/div[2]/table')
# html = web_page.get_attribute('OuterHTML')