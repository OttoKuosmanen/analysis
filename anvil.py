import pandas as pd
from scipy.stats import kruskal
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# DATAFILE
file_path = 'data/study3/data_2023_12_8.csv'

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
GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]

# Split groups
Human_helpfulness = Human[[col for col in Human.columns if col.endswith('1')]]
Human_effectiveness = Human[[col for col in Human.columns if col.endswith('2')]]
Human_appropriateness = Human[[col for col in Human.columns if col.endswith('3')]]
Human_sensitivity = Human[[col for col in Human.columns if col.endswith('4')]]

GPT3_helpfulness = GPT3[[col for col in GPT3.columns if col.endswith('1')]]
GPT3_effectiveness = GPT3[[col for col in GPT3.columns if col.endswith('2')]]
GPT3_appropriateness = GPT3[[col for col in GPT3.columns if col.endswith('3')]]
GPT3_sensitivity = GPT3[[col for col in GPT3.columns if col.endswith('4')]]

GPTchat_helpfulness = GPTchat[[col for col in GPTchat.columns if col.endswith('1')]]
GPTchat_effectiveness = GPTchat[[col for col in GPTchat.columns if col.endswith('2')]]
GPTchat_appropriateness = GPTchat[[col for col in GPTchat.columns if col.endswith('3')]]
GPTchat_sensitivity = GPTchat[[col for col in GPTchat.columns if col.endswith('4')]]

GPT4_helpfulness = GPT4[[col for col in GPT4.columns if col.endswith('1')]]
GPT4_effectiveness = GPT4[[col for col in GPT4.columns if col.endswith('2')]]
GPT4_appropriateness = GPT4[[col for col in GPT4.columns if col.endswith('3')]]
GPT4_sensitivity = GPT4[[col for col in GPT4.columns if col.endswith('4')]]

# Remove 0 TOTALS
data_Human = Human.values.flatten()[Human.values.flatten() != 0]
data_GPT3 = GPT3.values.flatten()[GPT3.values.flatten() != 0]
data_GPTchat = GPTchat.values.flatten()[GPTchat.values.flatten() != 0]
data_GPT4 = GPT4.values.flatten()[GPT4.values.flatten() != 0]

# SCALE POINTS
data_human_helpfulness = Human_helpfulness.values.flatten()[Human_helpfulness.values.flatten() != 0]
data_human_effectiveness = Human_effectiveness.values.flatten()[Human_effectiveness.values.flatten() != 0]
data_human_appropriateness = Human_appropriateness.values.flatten()[Human_appropriateness.values.flatten() != 0]
data_human_sensitivity = Human_sensitivity.values.flatten()[Human_sensitivity.values.flatten() != 0]

data_GPT3_helpfulness = GPT3_helpfulness.values.flatten()[GPT3_helpfulness.values.flatten() != 0]
data_GPT3_effectiveness = GPT3_effectiveness.values.flatten()[GPT3_effectiveness.values.flatten() != 0]
data_GPT3_appropriateness = GPT3_appropriateness.values.flatten()[GPT3_appropriateness.values.flatten() != 0]
data_GPT3_sensitivity = GPT3_sensitivity.values.flatten()[GPT3_sensitivity.values.flatten() != 0]

data_GPTchat_helpfulness = GPTchat_helpfulness.values.flatten()[GPTchat_helpfulness.values.flatten() != 0]
data_GPTchat_effectiveness = GPTchat_effectiveness.values.flatten()[GPTchat_effectiveness.values.flatten() != 0]
data_GPTchat_appropriateness = GPTchat_appropriateness.values.flatten()[GPTchat_appropriateness.values.flatten() != 0]
data_GPTchat_sensitivity = GPTchat_sensitivity.values.flatten()[GPTchat_sensitivity.values.flatten() != 0]

data_GPT4_helpfulness = GPT4_helpfulness.values.flatten()[GPT4_helpfulness.values.flatten() != 0]
data_GPT4_effectiveness = GPT4_effectiveness.values.flatten()[GPT4_effectiveness.values.flatten() != 0]
data_GPT4_appropriateness = GPT4_appropriateness.values.flatten()[GPT4_appropriateness.values.flatten() != 0]
data_GPT4_sensitivity = GPT4_sensitivity.values.flatten()[GPT4_sensitivity.values.flatten() != 0]

# Calculate the average for each group and rating scale
averages = [
    np.mean(data_human_helpfulness), np.mean(data_GPT3_helpfulness),
    np.mean(data_GPTchat_helpfulness), np.mean(data_GPT4_helpfulness),
    np.mean(data_human_effectiveness), np.mean(data_GPT3_effectiveness),
    np.mean(data_GPTchat_effectiveness), np.mean(data_GPT4_effectiveness),
    np.mean(data_human_appropriateness), np.mean(data_GPT3_appropriateness),
    np.mean(data_GPTchat_appropriateness), np.mean(data_GPT4_appropriateness),
    np.mean(data_human_sensitivity), np.mean(data_GPT3_sensitivity),
    np.mean(data_GPTchat_sensitivity), np.mean(data_GPT4_sensitivity)
]

# Create a list of labels for the box plots (to distinguish the groups)
labels = [
    "Human (Helpfulness)", "GPT3 (Helpfulness)", "GPTchat (Helpfulness)", "GPT4 (Helpfulness)",
    "Human (Effectiveness)", "GPT3 (Effectiveness)", "GPTchat (Effectiveness)", "GPT4 (Effectiveness)",
    "Human (Appropriateness)", "GPT3 (Appropriateness)", "GPTchat (Appropriateness)", "GPT4 (Appropriateness)",
    "Human (Sensitivity)", "GPT3 (Sensitivity)", "GPTchat (Sensitivity)", "GPT4 (Sensitivity)"
]

# Create a bar chart
plt.figure(figsize=(12, 8))
plt.barh(labels, averages, color='skyblue')
plt.xlabel("Average Scaled Ratings")
plt.title("Average Scaled Ratings by Model and Rating Scale")

# Show the plot
plt.tight_layout()
plt.show()






"""
# Ratings list for Kruskal-Wallis test: Helpfulness
ratings_list_helpfulness = [data_human_helpfulness, data_GPT3_helpfulness, data_GPTchat_helpfulness, data_GPT4_helpfulness]

# Ratings list for Kruskal-Wallis test: Effectiveness
ratings_list_effectiveness = [data_human_effectiveness, data_GPT3_effectiveness, data_GPTchat_effectiveness, data_GPT4_effectiveness]

# Ratings list for Kruskal-Wallis test: Appropriateness
ratings_list_appropriateness = [data_human_appropriateness, data_GPT3_appropriateness, data_GPTchat_appropriateness, data_GPT4_appropriateness]

# Ratings list for Kruskal-Wallis test: Sensitivity
ratings_list_sensitivity = [data_human_sensitivity, data_GPT3_sensitivity, data_GPTchat_sensitivity, data_GPT4_sensitivity]

# SIGNIFICANCE TESTING #

# Perform Kruskal-Wallis test on total helpfulness
h_statistic, p_value = kruskal(*ratings_list_helpfulness)

# Check the p-value to determine significance
alpha = 0.001   # Set your significance level
if p_value < alpha:
    print("There are significant differences between the groups.")
else:
    print("There are no significant differences between the groups.")

"""