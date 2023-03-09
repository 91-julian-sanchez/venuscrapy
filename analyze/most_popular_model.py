import pandas as pd

# Read the CSV file
df = pd.read_csv("../output/load/latina.csv")

# Group the DataFrame by the model name, and then sum the 'viewers' and 'impression' columns
df_grouped = df.groupby('model').agg({ 'age': 'first', 'link': 'first', 'viewers': 'sum', 'impression': 'sum'})

# Sort the results in descending order by the total number of viewers and impressions, and then take the top 10 records
most_popular_models = df_grouped.sort_values(['viewers', 'impression'], ascending=False).head(10)

# Print the result
print("The top 10 most popular models are:")
print(most_popular_models)
print(most_popular_models.describe())