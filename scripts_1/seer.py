import pandas as pd
from collections import Counter


def count_strings(data, column,column2=None):
    country_list = []
    for item in data[column]:
        if pd.notna(item) and not item.startswith("Other"):
            country_list.append(item)
    if column2 is not None:        
        for item in data[column2]:
            if pd.notna(item):
                country_list.append(item)

        
    string_counts = Counter(country_list)
    return string_counts    



# DATAFILE
file_path = '../data/study1/data_2023_12_16.csv'

# Read the CSV file
df = pd.read_csv(file_path)


# Remove Rows
orb = df.drop([0, 1], axis=0)



# Chop columns to include only ratings
palantir = orb.iloc[:, 11:22]

land_data = count_strings(palantir,"Country","Country_9_TEXT")

gender_data = count_strings(palantir,"Gender","Gender_3_TEXT")

education_data = count_strings(palantir,"Education","Education_8_TEXT")

age_data = count_strings(palantir, "Age")