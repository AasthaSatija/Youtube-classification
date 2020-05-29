# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
import numpy as np

df = pd.read_csv('final_data.csv')

df['title'].replace({'\n' : ''}, inplace=True, regex=True) #remove the new line characters with space
for i, title in enumerate(df['title']):
    df.loc[i, 'title'] = title.strip() # whitespaces are removed starting and trailing from the title
    
df.dropna(axis=0, inplace=True)  # null values from the row

print('The shape of dataset after cleaning is: {}'.format(df.shape)) #returns rows and columns

df.to_csv('clean_data.csv')

