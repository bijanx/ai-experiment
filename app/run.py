import pandas as pd
import numpy as np

# load the data
df = pd.read_csv('dax.csv', dtype = {'DATE': str, 'TIME': str})
df.index = pd.to_datetime(df.DATE.str.cat(df.TIME, sep=' '), format="%Y%m%d %H:%M")
df = df.drop('DATE',1)
df = df.drop('TIME',1)
