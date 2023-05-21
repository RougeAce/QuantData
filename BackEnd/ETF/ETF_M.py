import pandas as pd
table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df2 = table[1]

print(df2.columns)

print(df2['Added']['Ticker'])
print(df2['Removed']['Ticker']) 