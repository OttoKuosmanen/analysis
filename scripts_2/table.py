import pandas as pd
from scipy.stats import chi2_contingency

# Functions

def table(observed, expected_ratio=0.5):
    # data_structure for observed [AI,Human]
    
    observed_counts = observed
    expected_counts = [sum(observed) * expected_ratio,sum(observed) * expected_ratio]

    data = {
        'Observed Counts': observed_counts,
        'Expected Counts': expected_counts
        }

    index = ['AI source indicated', 'Human source indicated']


    df = pd.DataFrame(data, index=index)
    return df

def perform_chi_square_test(observed_counts):
    # The observed counts are in the format [AI count, Human count]
    total = sum(observed_counts)
    expected_counts = [total / 2, total / 2]  # Assuming 50/50 split for expected counts

    chi2_statistic, p_value, _, _ = chi2_contingency([observed_counts, expected_counts])
    return chi2_statistic, p_value


# DATAFILE
file_path = '../data/study2/data_2023_12_11.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 23:-1]


# Group ratings
Human = ratings[[col for col in ratings.columns if col.lower().startswith('human')]]
GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]

# Count "Human" and "AI" for each group
human_human_count = (Human == 'Human').sum().sum()
human_ai_count = (Human == 'AI').sum().sum()
total_observations_human = human_human_count + human_ai_count

gpt3_human_count = (GPT3 == 'Human').sum().sum()
gpt3_ai_count = (GPT3 == 'AI').sum().sum()
total_observations_gpt3 = gpt3_ai_count + gpt3_human_count

gptchat_human_count = (GPTchat == 'Human').sum().sum()
gptchat_ai_count = (GPTchat == 'AI').sum().sum()
total_observations_gptchat = gptchat_ai_count + gptchat_human_count

gpt4_human_count = (GPT4 == 'Human').sum().sum()
gpt4_ai_count = (GPT4 == 'AI').sum().sum()
total_observations_gpt4 = gpt4_ai_count + gpt4_human_count

total_n = [total_observations_human, total_observations_gpt3, total_observations_gptchat, total_observations_gpt4]

# Print the counts
print("Human group - 'Human' count:", human_human_count, "'AI' count:", human_ai_count)
print("GPT3 group - 'Human' count:", gpt3_human_count, "'AI' count:", gpt3_ai_count)
print("GPTchat group - 'Human' count:", gptchat_human_count, "'AI' count:", gptchat_ai_count)
print("GPT4 group - 'Human' count:", gpt4_human_count, "'AI' count:", gpt4_ai_count)


# AI TOTALS
tt = gpt3_ai_count + gpt3_human_count + gpt4_ai_count + gpt4_human_count + gptchat_ai_count + gptchat_human_count
tc = gpt3_ai_count + gpt4_ai_count + gptchat_ai_count
ai_correct =  tc / tt
print(f"AI correct :{ai_correct}%")

# GPT 3
gpt3_correct = gpt3_ai_count / (gpt3_ai_count + gpt3_human_count)
print(f"gpt3 correct :{gpt3_correct}%")

# GPT3.5
gptchat_correct = gptchat_ai_count / (gptchat_ai_count + gptchat_human_count)
print(f"gpt3.5 correct :{gptchat_correct}%")

# GPT 4
gpt4_correct = gpt4_ai_count / (gpt4_ai_count + gpt4_human_count)
print(f"gpt4 correct :{gpt4_correct}%")

# Human
human_correct =  human_human_count / (human_human_count + human_ai_count)
print(f"Human correct :{human_correct}%")

# making tables
gpt3_observed = [gpt3_ai_count,gpt3_human_count]
gptchat_observed = [gptchat_ai_count,gptchat_human_count]
gpt4_observed = [gpt4_ai_count,gpt4_human_count]
human_observed = [human_ai_count,human_human_count]
AI_observed = [gpt3_ai_count+gptchat_ai_count+gpt4_ai_count,gpt3_human_count+gptchat_human_count+gpt4_human_count]


df_gpt3 = table(gpt3_observed)
df_gptchat = table(gptchat_observed)
df_gpt4 = table(gpt4_observed)
df_human = table(human_observed)
df_AI = table(AI_observed)

# Individual tests
chi2_gpt3, p_gpt3 = perform_chi_square_test(gpt3_observed)
chi2_gptchat, p_gptchat = perform_chi_square_test(gptchat_observed)
chi2_gpt4, p_gpt4 = perform_chi_square_test(gpt4_observed)
chi2_human, p_human = perform_chi_square_test(human_observed)
chi2_ai, p_ai = perform_chi_square_test(AI_observed)

# You can print these values to see the results
print("GPT-3 Chi-Square:", chi2_gpt3, "P-Value:", p_gpt3)
print("GPTchat Chi-Square:", chi2_gptchat, "P-Value:", p_gptchat)
print("GPT-4 Chi-Square:", chi2_gpt4, "P-Value:", p_gpt4)
print("Human Chi-Square:", chi2_human, "P-Value:", p_human)
print("Aggregated AI Chi-Square:", chi2_ai, "P-Value:", p_ai)

