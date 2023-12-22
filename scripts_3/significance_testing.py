import pandas as pd
import numpy as np
from scipy.stats import kruskal
from scipy.stats import mannwhitneyu

# functions

def perform_stat_test(test_data, test_name, alpha=0.003, test_type='mannwhitneyu'):
    print(f"_____________________{test_name}____________________")
    if test_type == 'mannwhitneyu':
        u_statistic, p_value = mannwhitneyu(*test_data)
    elif test_type == 'kruskal':
        h_statistic, p_value = kruskal(*test_data)

    print(f"p-value = {p_value}")
    if p_value < alpha:
        print("There are significant differences between the groups.")
    else:
        print("There are no significant differences between the groups.")
    print("____________________________________________________\n")
    
# DATAFILE
file_path = '../data/study3/data_2023_12_11.csv'

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

# Total observations
total_human = len(data_Human)
total_gpt3 = len(data_GPT3)
total_gptchat = len(data_GPTchat)
total_gpt4 = len(data_GPT4)

# Group ratings
Human = ratings[[col for col in ratings.columns if col.lower().startswith('human')]]
AI = ratings[[col for col in ratings.columns if col.lower().startswith('gpt')]]



# Remove 0 TOTALS
data_Human = Human.values.flatten()[Human.values.flatten() != 0]
data_AI = AI.values.flatten()[AI.values.flatten() != 0]


# SCALE POINTS

#HUMAN
data_human_helpfulness = Human_helpfulness.values.flatten()[Human_helpfulness.values.flatten() != 0]
data_human_effectiveness = Human_effectiveness.values.flatten()[Human_effectiveness.values.flatten() != 0]
data_human_appropriateness = Human_appropriateness.values.flatten()[Human_appropriateness.values.flatten() != 0]
data_human_sensitivity = Human_sensitivity.values.flatten()[Human_sensitivity.values.flatten() != 0]



#GPT3
data_GPT3_helpfulness = GPT3_helpfulness.values.flatten()[GPT3_helpfulness.values.flatten() != 0]
data_GPT3_effectiveness = GPT3_effectiveness.values.flatten()[GPT3_effectiveness.values.flatten() != 0]
data_GPT3_appropriateness = GPT3_appropriateness.values.flatten()[GPT3_appropriateness.values.flatten() != 0]
data_GPT3_sensitivity = GPT3_sensitivity.values.flatten()[GPT3_sensitivity.values.flatten() != 0]
#GPTchat
data_GPTchat_helpfulness = GPTchat_helpfulness.values.flatten()[GPTchat_helpfulness.values.flatten() != 0]
data_GPTchat_effectiveness = GPTchat_effectiveness.values.flatten()[GPTchat_effectiveness.values.flatten() != 0]
data_GPTchat_appropriateness = GPTchat_appropriateness.values.flatten()[GPTchat_appropriateness.values.flatten() != 0]
data_GPTchat_sensitivity = GPTchat_sensitivity.values.flatten()[GPTchat_sensitivity.values.flatten() != 0]
#GPT4
data_GPT4_helpfulness = GPT4_helpfulness.values.flatten()[GPT4_helpfulness.values.flatten() != 0]
data_GPT4_effectiveness = GPT4_effectiveness.values.flatten()[GPT4_effectiveness.values.flatten() != 0]
data_GPT4_appropriateness = GPT4_appropriateness.values.flatten()[GPT4_appropriateness.values.flatten() != 0]
data_GPT4_sensitivity = GPT4_sensitivity.values.flatten()[GPT4_sensitivity.values.flatten() != 0]

# AI Totals for each scale
data_AI_helpfulness = np.concatenate([data_GPT3_helpfulness, data_GPTchat_helpfulness, data_GPT4_helpfulness])
data_AI_effectiveness = np.concatenate([data_GPT3_effectiveness, data_GPTchat_effectiveness, data_GPT4_effectiveness])
data_AI_appropriateness = np.concatenate([data_GPT3_appropriateness, data_GPTchat_appropriateness, data_GPT4_appropriateness])
data_AI_sensitivity = np.concatenate([data_GPT3_sensitivity, data_GPTchat_sensitivity, data_GPT4_sensitivity])


# SIGNIFICANCE TESTING #

# ADVICE QUALITY
perform_stat_test([data_Human, data_AI], "Advice quality difference human and AI")
perform_stat_test([data_GPT3, data_GPTchat, data_GPT4], "Advice quality difference all AI models", test_type='kruskal')

perform_stat_test([data_Human, data_GPT3], "Advice quality single comparison GPT3/Human")
perform_stat_test([data_Human, data_GPTchat], "Advice quality single comparison GPT3.5/Human")
perform_stat_test([data_Human, data_GPT4], "Advice quality single comparison GPT4/Human")

# HELPFULNESS
perform_stat_test([data_human_helpfulness, data_AI_helpfulness], "Helpfulness difference between human and AI")
perform_stat_test([data_GPT3_helpfulness, data_GPTchat_helpfulness, data_GPT4_helpfulness], "Helpfulness difference among AI models", test_type='kruskal')


# EFFECTIVENESS
perform_stat_test([data_human_effectiveness, data_AI_effectiveness], "Effectiveness difference between human and AI")
perform_stat_test([data_GPT3_effectiveness, data_GPTchat_effectiveness, data_GPT4_effectiveness], "Effectiveness difference among AI models", test_type='kruskal')


# APPROPRIATENESS
perform_stat_test([data_human_appropriateness, data_AI_appropriateness], "Appropriateness difference between human and AI")
perform_stat_test([data_GPT3_appropriateness, data_GPTchat_appropriateness, data_GPT4_appropriateness], "Appropriateness difference among AI models", test_type='kruskal')


# SENSITIVITY
perform_stat_test([data_human_sensitivity, data_AI_sensitivity], "Sensitivity difference between human and AI")
perform_stat_test([data_GPT3_sensitivity, data_GPTchat_sensitivity, data_GPT4_sensitivity], "Sensitivity difference among AI models", test_type='kruskal')




