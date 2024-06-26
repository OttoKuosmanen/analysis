import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DATAFILE
file_path = '../data/study3/data_2023_12_16.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 22:-3]

# Fill NaN values with 0
ratings = ratings.fillna(0)

# Convert ratings to integers
ratings = ratings.astype(int)

# Group ratings
Human = ratings[[col for col in ratings.columns if col.lower().startswith('human')]]
GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]

# List only values different than 0, remowe empty data
data_Human = Human.values.flatten()[Human.values.flatten() != 0]
data_GPT3 = GPT3.values.flatten()[GPT3.values.flatten() != 0]
data_GPTchat = GPTchat.values.flatten()[GPTchat.values.flatten() != 0]
data_GPT4 = GPT4.values.flatten()[GPT4.values.flatten() != 0]


# Create histograms for rating distributions
plt.figure(figsize=(12, 8))

plt.subplot(221)
sns.histplot(data_Human, kde=True)
plt.title("Human Advice Quality Ratings", fontweight='bold')

plt.subplot(222)
sns.histplot(data_GPT3, kde=True)
plt.title("Text_Davinci_3 Advice Quality Ratings", fontweight='bold')

plt.subplot(223)
sns.histplot(data_GPTchat, kde=True)
plt.title("GPT3.5_Trubo Advice Quality Ratings", fontweight='bold')

plt.subplot(224)
sns.histplot(data_GPT4, kde=True)
plt.title("GPT4 Advice Quality Ratings", fontweight='bold')

plt.tight_layout()

plt.show()



