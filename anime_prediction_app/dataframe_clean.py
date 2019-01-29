import pandas as pd
import numpy as np
import re


df = pd.read_csv('data/data.csv')



for c in list(filter(lambda x: re.search('Unnamed:',x), df.columns)):
    df = df.drop(c, axis=1)

df = df.reset_index().drop('index', axis=1)

df.to_csv('data/data.csv')
