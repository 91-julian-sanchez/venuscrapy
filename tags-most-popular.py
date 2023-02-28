import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("output/chaturbate-latina-etl2.csv")
tag_list = ' '.join(df['tags']).replace(',','').split('#')

tag_count = {}
for tag in tag_list:
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1
        
sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)

tag_df = pd.DataFrame(sorted_tags, columns=["Tag", "Count"])
print(tag_df.head(50))

# tag_df.head(50).plot(kind='bar', x='Tag', y='Count', color='skyblue')
# plt.xlabel("Tag")
# plt.ylabel("Count")
# plt.title("Most popular tags")
# plt.show()