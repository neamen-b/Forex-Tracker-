import pandas as pd
from typing import Dict, List


class Analyze:

    # To be filled
    def __init__(self) -> None:
        self.merged_data_frame : pd.DataFrame = pd.DataFrame(columns= ['Currency'])

    # Merges on Currency* and is an outer join
    # There are disticnt columns for each dataframe
    def merge_dataframes (self, bank_tables : Dict[str, pd.DataFrame]) -> None:

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

            print(f'frame after rename')
            print(frame)
            # Merge currenct frame to aggregate frame on 'Currency'
            self.merged_data_frame = pd.merge(self.merged_data_frame, frame, on = 'Currency', how = 'outer')







    


# Concatenates vertically*. It stacks up the dataframes
# there are sets of columns that belong to the same dataframe
# # the sets are names after the name of the bank
# def concatenate_dataframes (data_frames: Dict[str , pd.DataFrame]) -> None:

#     result_frame = pd.concat(list(data_frames.values()), axis=0, keys= data_frames.keys(), ignore_index= True)

#     return result_frame