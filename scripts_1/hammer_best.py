import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency

# DATAFILE
file_path = '../data/study1/data_2023_12_16.csv'

# Read and preprocess the CSV file
df = pd.read_csv(file_path)
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)
data_ore = data_ore.drop([0, 1], axis=0)

# Group ratings by model
model_columns = {'GPT3': 'gpt3_', 'GPT3.5': 'gpt3.5', 'GPT4': 'gpt4'}
model_data = {model: data_ore[[col for col in data_ore.columns if col.lower().startswith(prefix)]]
              for model, prefix in model_columns.items()}

# Function to count AI and Human responses
def count_responses(data):
    human_count = data.isin(['Human', 'Human Answer']).sum().sum()
    ai_count = (data == 'AI').sum().sum()
    return ai_count, human_count

# Count responses for each model
counts = {model: count_responses(data) for model, data in model_data.items()}
total_counts = {model: sum(count) for model, count in counts.items()}
ai_counts, human_counts = zip(*[count for count in counts.values()])
total_ai = sum(ai_counts)
total_human = sum(human_counts)

# Print summary
print(f"Human chosen: {total_human} times")
print(f"AI chosen: {total_ai} times")
print(f"Human chosen: {total_human / (total_human + total_ai):.2%}")
print(f"AI chosen: {total_ai / (total_human + total_ai):.2%}")


# Signifiance tests
# Chi-square tests
def perform_chi_square_test(observed_counts, total_count):
    expected_counts = [total_count / 2, total_count / 2]
    chi2, p = chi2_contingency([observed_counts, expected_counts], correction=False)[:2]
    return chi2, p

# Test for each model
chi_square_results = {model: perform_chi_square_test(counts[model], total_counts[model]) 
                      for model in counts}
print(chi_square_results)

# Pooled test
pooled_observed_counts = np.array([total_ai, total_human])
pooled_expected_counts = np.array([total_ai + total_human] * 2) / 2
chi2_statistic, p_value = chi2_contingency([pooled_observed_counts, pooled_expected_counts], correction=False)[:2]
print("Pooled Test:", chi2_statistic, p_value)

# PLOTTING
plt.figure(figsize=(6, 6), facecolor="silver")
labels = ['AI Chosen', 'Human Chosen']
total_percentages = [total_ai / (total_ai + total_human) * 100, total_human / (total_ai + total_human) * 100]
bars = plt.bar(labels, total_percentages, color=['steelblue', 'salmon'], width=0.66)

# Add data labels on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}%', ha='center', va='bottom')


# Add a horizontal line at 50%
plt.axhline(y=50, color='black', linestyle='--')

# Add a label with the total count in between the bars
total_count_label = f'N: {total_ai + total_human}'
x_positions = [bar.get_x() + bar.get_width()/2 for bar in bars]
x_position = np.mean(x_positions)  # Midpoint between the bars
plt.text(x_position, 5, total_count_label, ha='center', va='bottom', fontsize=10, color='black')

# Determine the level of significance based on p-value and add the significance marker
if p_value < 0.05:
    significance_level = '***' if p_value < 0.001 else '**' if p_value < 0.01 else '*'
    y_position = max(total_percentages) + 2  # Adjust as necessary
    plt.text(x_position, y_position, significance_level, ha='center', va='bottom', fontsize=16)

# Other plot settings
plt.ylabel('Percentage')
plt.title('Preference for AI vs. Human Advice')
plt.ylim(0, 100)  # Set the y-axis limit to 100%

plt.show()




