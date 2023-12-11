import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal

# DATAFILE
file_path = '../data/study2/data_2023_12_9.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 23:-1]

""" read comments
for comment in df['Comment']:
    print(comment)
"""

# Group ratings
Human = ratings[[col for col in ratings.columns if col.lower().startswith('human')]]
GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]

# Count "Human" and "AI" for each group
human_human_count = (Human == 'Human').sum().sum()
human_ai_count = (Human == 'AI').sum().sum()

gpt3_human_count = (GPT3 == 'Human').sum().sum()
gpt3_ai_count = (GPT3 == 'AI').sum().sum()

gptchat_human_count = (GPTchat == 'Human').sum().sum()
gptchat_ai_count = (GPTchat == 'AI').sum().sum()

gpt4_human_count = (GPT4 == 'Human').sum().sum()
gpt4_ai_count = (GPT4 == 'AI').sum().sum()

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


# Create a bar plot to visualize the rates of correct identification for each model
models = ['Human', 'GPT3', 'GPT3.5', 'GPT4', 'AI Total']
correct_rates = [human_correct, gpt3_correct, gptchat_correct, gpt4_correct, ai_correct]

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=models, y=correct_rates, palette='viridis')
plt.title('Correctly identified as AI or Human')
plt.ylim(0, 1)  # Set y-axis limit from 0 to 1
plt.ylabel('Correct Identification Rate')
plt.xlabel('Models')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the percentages on top of the bars
for i, rate in enumerate(correct_rates):
    plt.text(i, rate + 0.02, f'{rate*100:.2f}%', ha='center', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()

