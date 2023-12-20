import numpy as np
import pandas as pd
from scipy.stats import chi2

# Function to calculate the Chi-Squared statistic and p-value
def calculate_chi_squared(observed_counts):
    total = observed_counts.sum()
    expected_counts = np.array([total / 2, total / 2])
    chi_squared_stat = ((observed_counts - expected_counts) ** 2 / expected_counts).sum()
    p_value = chi2.sf(chi_squared_stat, df=1)  # df=1 for one degree of freedom
    return chi_squared_stat, p_value

# Function to count AI and Human responses
def count_responses(data):
    human_count = data.isin(['Human', 'Human Answer']).sum().sum()
    ai_count = (data == 'AI').sum().sum()
    return ai_count, human_count

# Main function to run the analysis
def run_analysis(file_path):
    # Read and preprocess the CSV file
    df = pd.read_csv(file_path)
    data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)
    data_ore = data_ore.drop([0, 1], axis=0)

    # Group ratings by model
    model_columns = {'GPT3': 'gpt3_', 'GPT3.5': 'gpt3.5_', 'GPT4': 'gpt4_'}
    model_data = {model: data_ore[[col for col in data_ore.columns if col.lower().startswith(prefix)]]
                  for model, prefix in model_columns.items()}

    # Count responses for each model and calculate Chi-Squared statistics and p-values
    chi_squared_results = {}
    for model, data in model_data.items():
        counts = count_responses(data)
        chi_squared_results[model] = calculate_chi_squared(np.array(counts))

    # Calculate pooled Chi-Squared statistics and p-values
    pooled_counts = count_responses(data_ore)
    pooled_chi_squared_result = calculate_chi_squared(np.array(pooled_counts))

    return chi_squared_results, pooled_chi_squared_result

# This if statement ensures that the following code will run only if the script is executed directly,
# and not when it is imported as a module.
if __name__ == "__main__":
    file_path = '../data/study1/data_2023_12_16.csv'
    results, pooled_result = run_analysis(file_path)

    # Output the results
    print("Chi-Squared Results for Each Model:")
    for model, result in results.items():
        print(f"{model}: Chi-Squared Statistic = {result[0]}, p-value = {result[1]}")

    print(f"\nPooled Chi-Squared Result: Chi-Squared Statistic = {pooled_result[0]}, p-value = {pooled_result[1]}")
