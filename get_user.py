import pandas as pd

df = pd.read_csv('./highest_clean.csv', engine='python')['author']
print('finished read')
pd.DataFrame(pd.unique(df)).to_csv('unique_users.csv',sep=',', index=False)
print('finished file execution')

