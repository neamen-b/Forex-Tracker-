import json
from Scraper import ForexScraper
from Analyses import Analyze
from typing import Dict, Optional, Union
import pandas as pd

class Storer:

    # Dependency injection
    # gave this class instances of Analyze and ForexScraper that have the data to be stored
    def __init__(self, analyses : Analyze, scraper: ForexScraper) -> None:
        self.analyze = analyses
        self.scrape = scraper

    def store (self) -> None:
        '''
        Top level dictionary:
            Name of data : Dictionary of data
        
        Second Level dictionary (Dictionary of Data)
            Data type : Dataframe in Dictionary form

        Typing has to be fixed here
        '''
        all_data : Dict [str, Dict[str, Optional[Dict]]] = {}

        # Dictionary of data_name to Dictionary of transaction type to Dictionary form of filtered dataframe
        # Dictionary Comprehension
        # Makes a copy of the dataframes then changes to dictionary
        # Replaces all NaN will null for json 
        # where notnull is false, replace wtih None
        # where (condition, other) -> if conidtion true, keeo, else replace with other

        # temp_filtered = self.analyze.filtered_df.astype(str)

        # Horridly inefficient with conveting values to strings in the df so that it gets null for json
        all_data['Filtered'] = {name : data_frame.copy().astype(str).where(pd.notnull(data_frame), None).to_dict() for name, data_frame in self.analyze.filtered_df.items()}
        # map(function = lambda x : x.copy().to_dict(), iter = list(self.analyze.filtered_df.values()))

        # Horridly inefficient with conveting values to strings in the df so that it gets null for json
        # Dictionary of data_name to Dictionary of transaction type to Dictionary form of stattisctics dataframe
        all_data['Stats'] = {name : data_frame.copy().astype(str).where(pd.notnull(data_frame), None).to_dict() for name , data_frame in self.analyze.statistics_df.items()}

        # Dictionary of data_name to Dictionary of bank anme to Dictionary form of tables dataframe
        # The NaN replacement workhere for Rates and Aggregate because they don't have float values
        all_data['Rates'] = {name : data_frame.copy().where(pd.notnull(data_frame), None).to_dict() for name , data_frame in self.scrape.bank_tables_dataframe.items()}

        # Dcitionary of data_name to merged dataframe in Dictionary form
        all_data['Aggregate'] = self.scrape.merged_data_frame.copy().where(pd.notnull(self.scrape.merged_data_frame), None).to_dict()

        # Dictionary of a dictionary with black data
        all_data['Black'] = self.scrape.black_market_data

        myfile = open(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\all_data.json', 'w')
        json.dump(all_data, myfile)

        myfile.close()

        # return all_data





        