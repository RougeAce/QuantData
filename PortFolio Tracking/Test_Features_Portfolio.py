import pandas as pd

# Create a DataFrame with one row
df = pd.DataFrame({'Asset': ['Cash'], 'Value': [100000]})

# Add a new row to the DataFrame
df.loc[len(df)] = ['BTC', 50000]

# Print the updated DataFrame
print(df)
