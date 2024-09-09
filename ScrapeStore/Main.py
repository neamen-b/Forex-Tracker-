from Scraper import ForexScraper
from Analyses import Analyze
from Storage import Storer
import json
import pandas as pd

scrape = ForexScraper()

scrape.Awash('https://awashbank.com/exchange-historical/')
scrape.CBE('https://www.combanketh.et/en/exchange-rate/')
scrape.COOP('https://coopbankoromia.com.et/daily-exchange-rates/')
scrape.Dashen('https://dashenbanksc.com/daily-exchange-rates-2/')
scrape.Hijra('https://hijra-bank.com/')
scrape.NIB('https://www.nibbanksc.com/exchange-rate/')
scrape.Wegagen('https://wegagen.com/')

scrape.ETB_Black_Market('https://ethioblackmarket.com/')
# print(f"Black market - {scrape.black_market_data}")

scrape.Chrome_Driver.quit()

scrape.merge_dataframes()
# print(f"merged data frame {scrape.merged_data_frame.head()}")

# This is the merge data frames part
# Saves in Json
analyze = Analyze()
# analyze.merge_dataframes(scrape.bank_tables_dataframe)
# analyze.merged_data_frame.to_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\merged.json')

# Reads in the json file with the merged dataframe and initializes a new dataframe
# merged_rates_data_frame = pd.read_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\merged.json')
# merged_rates_data_frame.to_csv(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\merge.csv')
# print(merged_rates_data_frame.head())

# print("Merged df before stats")
# print(scrape.merged_data_frame.head())

# Saving the merged to see if there is a difference with the other saved one
# print(scrape.merged_data_frame.to_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\aggregate.json'))


analyze.stats(scrape.merged_data_frame)
# print("Filtered \n", analyze.filtered_df)
# print("Stats \n ", analyze.statistics_df)

s = Storer(analyses= analyze, scraper=scrape)
s.store()
 