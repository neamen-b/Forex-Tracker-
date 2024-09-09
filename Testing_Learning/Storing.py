import pandas as pd
import json
import numpy as np
from datetime import date, datetime

df1 = pd.DataFrame({
    'A' : [1,2,3,np.nan,5],
    'B' : [6,7,8,np.nan,10],
    'C' : ['A', 'B', 'C', 'D', 'E']
})


df2 = pd.DataFrame({
    'D':[45,6,778,54],
    'E' : [45, 54645.7, 66756, 7587]
})


dict_of_dfs = {'df1' : df1, 'df2': df2}
# print("type before coversion:", lambda x : type(x) in list(dict_of_dfs.values()))
# print(dict_of_dfs['df1'].to_dict())

# Dictionary comprehension
# Keep the same key but apply to_dict() to the the copies of the dataframe
# Copying to preserve parameters
dict_of_dfs_2 = {key : value.astype(str).copy().where(pd.notnull(value), None).to_dict() for key , value in dict_of_dfs.items()}

# map(lambda x: x.to_dict(), list(dict_of_dfs.values()))
print("Dataframe:", dict_of_dfs)
print("Dictionary:", dict_of_dfs_2)



file_name = str(date.today())
current_time = str(datetime.now().time())
print(file_name)
print(current_time)


myfile = open(fr'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\Testing_Learning\{file_name}.json', 'w')

json.dump(dict_of_dfs_2['df1'], myfile)
# Filename and path of storage
# file_name = r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\Testing_Learning\test_json.json'

# Creates a .json file in the given directory with the given name
# myfile = open(file_name, 'w')

# .dump() takes in a dcitionary, and file object
# converted dataframe to dictionary with to_dict()
# json.dump(df1.to_dict(), myfile)
# myfile.write('\n')
# json.dump(df2.to_dict(), myfile)

# df1.to_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\Testing_Learning\to_json.json')