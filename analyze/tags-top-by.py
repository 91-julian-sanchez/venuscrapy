import pandas as pd
import numpy as np

df = pd.read_csv("output/chaturbate-latina-etl.csv")
tag_list = ' '.join(df['tags']).replace(',','').split('#')

tag_count = {}
for tag in tag_list:
    if tag in tag_count:
        tag_count[tag] += df.loc[df['tags'].str.contains(tag), 'viewers'].sum()
    else:
        tag_count[tag] = df.loc[df['tags'].str.contains(tag), 'viewers'].sum()
        
sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_tags)

tag_df = pd.DataFrame(sorted_tags, columns=["Tag", "Count"])
print(tag_df.head(50))
