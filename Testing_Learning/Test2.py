import pandas as pd

df1 = pd.DataFrame({
    'Currency': ['USD', 'GBP', 'EUR', 'CHF', 'SEK'],
    'Cash Buying': [104.22, 133.57, 114.20, 119.26, 9.91],
    'Cash Selling': [116.72, 149.60, 127.91, 133.57, 11.10]
})


df1['Currency'] = ['US Dollar', 'Pound Sterling', 'Euro', 'Chinese', 'Sequoia']

df1.to_json(r'C:\Users\Neamen\Documents\GitHub\Forex-Tracker-\Testing_Learning\test.json')