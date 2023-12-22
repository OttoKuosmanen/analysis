import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import numpy as np

# DATAFILE
file_path = '../data/study3/data_2023_12_11.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = data_ore.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 22:-3]

# Fill NaN values with 0
ratings = ratings.fillna(0)

# Convert ratings to integers
ratings = ratings.astype(int)

# Group ratings
Human = ratings[[col for col in ratings.columns if col.lower().startswith('human')]]
AI = ratings[[col for col in ratings.columns if col.lower().startswith('gpt')]]



# Remove 0 TOTALS
data_Human = Human.values.flatten()[Human.values.flatten() != 0]
data_AI = AI.values.flatten()[AI.values.flatten() != 0]


# Calculate the average for each group
avg_Human = np.mean(data_Human)
avg_AI = np.mean(data_AI)

# Create a list of labels for the bar plots
labels = ['Human', 'AI']

# Create a bar chart
plt.figure(figsize=(12, 8))
plt.bar(labels, [avg_Human, avg_AI], color='skyblue')
plt.xlabel("Average Scaled Ratings")
plt.ylabel("Groups")
plt.title("Average Scaled Ratings by Model and Rating Scale")

# Show the plot
plt.tight_layout()
plt.show()

# CHECKING
print(len(data_Human))
print(len(data_AI))

# Convert to int
int_list = [int(item) for item in data_Human]

int_list1 = [int(item) for item in data_AI]
