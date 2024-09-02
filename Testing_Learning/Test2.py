import pandas as pd
import re
df1 = pd.DataFrame({
    'Currency_A': ['USD_A', 'GBP_B', 'EUR_C', 'CHF_D', 'SEK_E'],
    'Cash Buying_B': [104.22, 133.57, 114.20, 119.26, 9.91],
    'Cash Selling_C': [116.72, 149.60, 127.91, 133.57, 11.10]
})


# df1['Currency'] = ['US Dollar', 'Pound Sterling', 'Euro', 'Chinese', 'Sequoia']

# df1.to_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\Testing_Learning\test.json')

df1 = df1.rename(columns = lambda x : x.lower())

print(df1)