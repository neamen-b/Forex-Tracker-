import Scraper
from Scraper import ForexScraper
from Analyses import Analyze
import pandas as pd
import json


scrape = ForexScraper()

scrape.Awash('https://awashbank.com/exchange-historical/')
scrape.COOP('https://coopbankoromia.com.et/daily-exchange-rates/')
scrape.Dashen('https://dashenbanksc.com/daily-exchange-rates-2/')
scrape.Hijra('https://hijra-bank.com/')
scrape.NIB('https://www.nibbanksc.com/exchange-rate/')
scrape.Wegagen('https://wegagen.com/')
scrape.CBE('https://www.combanketh.et/en/exchange-rate/')

# scrape.ETB_Black_Market('https://ethioblackmarket.com/')
# print(scrape.black_market_data)
scrape.Chrome_Driver.quit()

analyze = Analyze()
analyze.merge_dataframes(scrape.bank_tables_dataframe)
analyze.merged_data_frame.to_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\merged.json')

# Analyses.concatenate_dataframes(scrape.bank_tables_dataframe)


