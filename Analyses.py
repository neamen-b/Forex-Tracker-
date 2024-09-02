import pandas as pd
from typing import Dict, List
import re


class Analyze:

    # To be filled
    def __init__(self) -> None:
        # Stores filtered data frame
        self.filtered_df : Dict [str, pd.DataFrame] = {}
        # Stores stats of filtered dataframes
        self.statistics_df : Dict [str, pd.DataFrame] = {}

    # Takes in the merged dataframe and fills two Dictionaries
    # filtered_df  is the merged_dataframe filtered by transaction type
    # statistics_df is the stats for those filtered dataframes
    def stats (self, merged_data_frame : pd.DataFrame) -> None:
        
        # This functions takes in the merged_Dataframe with all the banks and their rates
        # Now, to compare, we have to group those columns by by cash/transactional and selling/buying
        # The list below has the different types of transactions in strings
        # The program uses each string to fileter the merged dataframe
        column_names : List[str] = ['Cash Buying', 'Cash Selling', 'Transactional Buying', 'Transactional Selling']

        '''
        This dictionary stores:
            Key : Which type of transaction i.e., Cash Buying/Selling or Transacational Buying/Selling
            Value: A dataframe with:
                a. Highest rate
                b. Name of the bank with highest rate
                c. Lowest rate
                d. Name of the bank with lowest rate
                e. Standard deviation
                f. Average rate
                e. Range of rates
        '''
        # stats_frames : Dict[str, pd.DataFrame] = {}


        # Filter the dataframe by the column name
        # Using regex
        for column_head in column_names:
            # f string regex string
            # using 'fr'
            # filter(regex=) looks for labels/column names that match the regex string provided
            # 'f' is used to embed the variable regex string
            # Currency label will not be included in this df
            filtered_data_frame = pd.DataFrame(merged_data_frame.filter(regex= fr'{column_head}'))

            # troubshooting data type issue
            # print("Filtered data frame before the column 'Currency' has been added")
            # print(f"tran type {column_head}")
            # print(filtered_data_frame.head())
            # Save each filetered df as json named by transaction type
            # filtered_data_frame.to_json(fr'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\filtered_{column_head}.json')

            # Cannot compare string type values with arithmetic operators 
            # turn each data point in every row to float type
            # float(x) does not work here because it not meant to handle the Dataframe data structure
            # apply() takes in a pandas series (basically a array/list) one by one and applies lambda to the whole thing
            # Does not modify the df in place so need to reassign it to df
            filtered_data_frame = filtered_data_frame.apply(lambda x : x.astype(float), axis=1)


            # print(filtered_data_frame.head())

            # Initializing stats df 
            df = pd.DataFrame()
            # Giving it the currency column
            df['Currency'] = merged_data_frame['Currency']

            # Highest value from all banks
            # axis = 1 means for each row which is currency in this case
            # skipna = True means skip Nan values when comparing
            df['Highest'] = filtered_data_frame.max(axis=1, skipna = True)

            # label (bank) of the lowest occurence
            # Since the labels are like 'Cash Buying_bankname, just looks for the 'bankname part'
            # idxmax gets the index of the highest
            # uses regex to search patterns in each row, each label name
            df['Highest_Bank'] = filtered_data_frame.idxmax(axis=1, skipna= True).apply(lambda x: ''.join(re.findall(pattern = r'_(.*)', string = x)))
            df['Lowest'] = filtered_data_frame.min(axis=1, skipna= True)
            df['Lowest_Bank'] = filtered_data_frame.idxmin(axis=1, skipna=True).apply(lambda x : ''.join(re.findall(pattern = r'_(.*)', string = x)))
            df['STD'] = filtered_data_frame.std(axis=1, skipna=True)
            df['Average'] = filtered_data_frame.mean(axis=1, skipna=True)
            df['Range'] = filtered_data_frame.max(axis=1, skipna=True) - filtered_data_frame.min(axis=1, skipna=True)

            # transaction type with the relates stats
            self.statistics_df[column_head] = df

            # Cleaning labels
            # Just bank name instead of full column name
            # rename applies the given function to each label
            # it also take a dict of changes
            filtered_data_frame = filtered_data_frame.rename(columns = lambda x : ''.join(re.findall(pattern= r'_(.*)', string= x)))
            # print(F"iloc -> \n {filtered_data_frame.columns}")

        # Bring back currency label
        # This is used to insert at a specific index
        # loc takes an index 0...n
        # column takes label name
        # value takes series
        # Insert is in place, returns None
        filtered_data_frame.insert(loc= 0, column='Currency', value= merged_data_frame['Currency'])
        # print(f"filtered dataframe after inserting currency at {column_head}")
        # print(filtered_data_frame.head())
        # Push to dictionary of filtered df for each transaction type 
        self.filtered_df[column_head] = filtered_data_frame

        


    


# Concatenates vertically*. It stacks up the dataframes
# there are sets of columns that belong to the same dataframe
# # the sets are names after the name of the bank
# def concatenate_dataframes (data_frames: Dict[str , pd.DataFrame]) -> None:

#     result_frame = pd.concat(list(data_frames.values()), axis=0, keys= data_frames.keys(), ignore_index= True)

#     return result_frame