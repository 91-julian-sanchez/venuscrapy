from os import walk
import os

files = next(walk('./output/extract'), (None, None, []))[2]  # [] if no file
for file in files:
    print((file.replace("chaturbate-latina-", "")).replace(".csv", ""))
    date = (file.replace("chaturbate-latina-", "")).replace(".csv", "")
    os.system(f"python etl.py --tag latina --timestamp {date}")