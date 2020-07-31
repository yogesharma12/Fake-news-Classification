import pandas as pd
import numpy as np
import string
import re
import nltk
from nltk.corpus import stopwords
nltk_stopwords = stopwords.words('english')
remove_punctuation = '!"$%&\'()*+,-./:;<=>?@[\\]“”^_`{|}~’'

def clean_column(dataframe, column_to_clean, new_col):
    df_copy = dataframe.copy()
    df_copy['copied_column'] = df_copy[column_to_clean]
    df_copy['copied_column'] = df_copy['copied_column'].str.lower()
    cleaned_column = []
    for label in df_copy.index:
        row = df_copy.loc[label, :]['copied_column']
        row = str(row)

        clean = re.sub('\W+', ' ',row)
        clean = re.sub('[0-9]+', '',clean)
        clean = clean.split()

        final_clean = ""
        for words in clean:
            #print(words)
            #print(" ")
            if not words in nltk_stopwords:
                final_clean+=" "+words

        #print(row)
        



        cleaned_column.append(final_clean)
    df_copy[new_col] = cleaned_column
    del df_copy['copied_column']
    return df_copy