# import pandas as pd
# import numpy as np

# df = pd.read_csv("output/chaturbate-latina-sort.csv")

# # Count the number of times each tag appears in the "tags" column
# tag_counts = df['tags'].str.split(',').explode().value_counts()
# top = None 
# top = 20
# print(f"Top {top} ", "="*30)
# print(tag_counts[:top])

# # A continuación, agrupamos los datos por edad y tags
# df['tag_list'] = df['tags'].str.split(',')
# df = df.explode('tag_list')
# age_by_tag = df.groupby('tag_list')['age'].mean().reset_index().rename(columns={"age": "mean_age"})
# age_by_tag['mean_age'] = np.floor(age_by_tag['mean_age']).astype(int)
# print(age_by_tag)
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("output/chaturbate-latina-sort.csv")

# Count the number of times each tag appears in the "tags" column
tag_counts = df['tags'].str.split(',').explode().value_counts()

# Calculate the average age for each tag
df['tag_list'] = df['tags'].str.split(',')
df = df.explode('tag_list')
age_by_tag = df.groupby('tag_list')['age'].mean().reset_index()

# Merge the two results into one DataFrame
result = pd.DataFrame({'tag': tag_counts.index, 'count': tag_counts.values})
result = result.merge(age_by_tag, left_on='tag', right_on='tag_list', how='left')
result['mean_age'] = result['age'].round().astype(int)
# Mostrar solo los primeros 20 resultados
result = result[:20]

# Plot the results
plt.bar(result['tag'], result['count'], color='blue')
plt.xlabel("Tag")
plt.xticks(rotation=90)
plt.ylabel("Count")
plt.title("Tag Counts and Average Age")

# Annotate the bar chart with the mean age for each tag
for i, row in result.iterrows():
    plt.text(i, row['count'], str(row['mean_age']), ha='center', color='red')

plt.show()