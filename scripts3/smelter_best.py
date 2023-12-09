import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal

# DATAFILE
file_path = '../data/study1/data_2023_12_9.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 22:-2]

"""
 #read comments
for comment in df['Comment']:
    print(comment)
"""


# Problem Human answer ! Human instance 1

# Group ratings

GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]


# Count "Human" and "AI" for each group

gpt3_human_count = (GPT3 == 'Human').sum().sum()
gpt3_ai_count = (GPT3 == 'AI').sum().sum()

gptchat_human_count = (GPTchat == 'Human').sum().sum()
gptchat_ai_count = (GPTchat == 'AI').sum().sum()

gpt4_human_count = (GPT4 == 'Human').sum().sum()
gpt4_ai_count = (GPT4 == 'AI').sum().sum()

# comparison
human_chosen = gpt3_human_count + gpt4_human_count + gptchat_human_count
ai_chosen = gpt3_ai_count + gpt4_ai_count + gptchat_ai_count

total = human_chosen + ai_chosen

print(f"Human chosen: {human_chosen} times")

print(f"AI chosen: {ai_chosen} times")


print(f"Human chosen: {human_chosen/total}%")
print(f"AI chosen: {ai_chosen/total}%")
