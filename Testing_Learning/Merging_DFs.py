import pandas as pd

# DataFrame from Bank 1
df1 = pd.DataFrame({
    'Currency': ['USD', 'GBP', 'EUR', 'CHF', 'SEK'],
    'Cash Buying': [104.22, 133.57, 114.20, 119.26, 9.91],
    'Cash Selling': [116.72, 149.60, 127.91, 133.57, 11.10]
})

# DataFrame from Bank 2
df2 = pd.DataFrame({
    'Currency': ['USD', 'GBP', 'EUR', 'CHF', 'SEK'],
    'Cash Buying': [104.08, 128.18, 114.43, 114.41, 9.45],
    'Cash Selling': [115.32, 142.69, 126.79, 127.35, 10.52]
})

# DataFrame from Bank 3
df3 = pd.DataFrame({
    'Currency': ['USD', 'GBP', 'EUR', 'CHF', 'SEK', 'NOK'],
    'Cash Buying': [104.30, 130.00, 113.50, 118.00, 9.70, 10.20],
    'Cash Selling': [117.00, 150.00, 127.50, 132.00, 10.90, 11.30]
})


data_frames = {'A': df1 , 'B': df2 , 'C':df3}
banks_names = list(data_frames.keys())
frames = list(data_frames.values())


merge = pd.DataFrame(columns= ['Currency'])

# # Create the merge dataframe witht he first dataframe
# merge = pd.DataFrame(dfs[0])

# # Rename all the columns to have the suffix of the first bank
# # Uses a lambda function
# # if columns is not currency, rename , else leave as is
# merge = merge.rename(columns= lambda x: x + '_' + banks_names[0] if x != 'Currency' else x)

# print(f"Merge Df after setting first df as merge and renaming columns to include suffixes")
# print(merge)


# Starting from index 1 beacuse i have already added the first dataframe
for count, data_frame in enumerate(frames):
    
    # Rename the columns name of each dataframe with the banks name except for the currency column
    # uses enumerates result to index bank names. Corresponds to each data frame
    data_frame = data_frame.rename(columns= lambda x : x + '_' + banks_names[count] if x != 'Currency' else x)

    #Don't need to worry about suffixes this way
    # Suffixes only applies a suffix if there is a conflict between the two merging dfs column names
    #merge = pd.merge(merge, df, on= 'Currency', how= 'outer', suffixes=('',"_"+banks_names[count]))

    merge = pd.merge(merge, data_frame, on='Currency', how='outer')

    print(banks_names[count])
    print(merge)

print(f'merge after all the dfs have been merged with suffixes added ') 
print(merge)





















# mydic = {"hello" : 1, "World" : 2}

# print(list(mydic.values()))

# # class test: 

# #     def __init__(self) -> None:
        
# #         self.name = "Name"
    
#     def push(self):
#         print(self.name)
    

# test = test()

# test.push()
