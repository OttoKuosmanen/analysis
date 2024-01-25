import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


# Plotting

# Define color palette
chosen_colors = ["#f7786b","#034f84","#034f84","#034f84"]

# Create a bar plot to visualize the rates of correct identification for each model
models = ['Human', 'GPT3', 'GPT3.5', 'GPT4']
correct_rates = [human_correct*100, gpt3_correct*100, gptchat_correct*100,gpt4_correct*100]

# Create a bar plot 
plt.figure(figsize=(8, 6))
sns.barplot(x=models, y=correct_rates, palette=chosen_colors)
plt.title('Correctly Identified Source', fontweight='bold', fontsize=24,pad=24)
plt.ylim(0, 1)  # Set y-axis limit from 0 to 1
plt.xlabel('Models', fontsize=24, fontweight="bold")
plt.xticks(fontsize=18)
plt.yticks([0,25,50,75,100], fontsize=20)
plt.axhline(y=50, color='black', linestyle='--')

#significance  symbol
x_position = 0  # X-coordinate for the "Human" bar
y_position = human_correct*100 + 5  # Y-coordinate slightly above the bar
significance_level = "***"  # Change this to your actual significance level


# Add text for significance level
plt.text(x_position, y_position +5, significance_level, ha='center', fontsize=20)


# Display the percentages and total_n on top of the bars
for i, (rate, total) in enumerate(zip(correct_rates, total_n)):
    plt.text(i, rate + 1, f'{rate:.1f}%', ha='center', fontsize=22)
    plt.text(i, 3, f'N: {total}', ha='center', fontsize=16, color="white", fontweight='bold')  # Adjust the vertical position here

# Show the plot
plt.tight_layout()
plt.show()

