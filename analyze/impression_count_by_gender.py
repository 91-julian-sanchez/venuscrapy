import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("../output/load/latina.csv")

# Group the DataFrame by gender, and sum the 'impression' column for each group
impression_by_gender = df.groupby('gender')['impression'].sum()

# Group the DataFrame by gender, and count the number of rows in each group
count_by_gender = df.groupby('gender').size()

# Combine the two previous DataFrames into a single one, with columns for impression sum and count
impression_count_by_gender = pd.concat([impression_by_gender, count_by_gender], axis=1, keys=['impression_sum', 'count'])

# Calculate the average impression count per influencer for each gender
impression_count_by_gender['average_impression'] = impression_count_by_gender['impression_sum'] / impression_count_by_gender['count']

# Print the resulting DataFrame
print(impression_count_by_gender)
