import pandas as pd

def clean_quotations (string):
    if isinstance(string, str): 
        final = string.replace('"', '').replace("'",'').replace('\\','')
        final = ' '.join(final.split())
        return final

keepcol = ['id','parent_id','subreddit_id','text','score','ups','author','controversiality']
df_highest = pd.read_csv('./highest_clean.csv', engine='python')[keepcol]
print('finished reading')
df_highest['text']= df_highest['text'].apply(clean_quotations)

print('finished cleanup')
df_highest.to_csv('highest_clean3.csv', sep=',', index=False)
print('finished export')
