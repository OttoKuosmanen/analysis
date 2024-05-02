import matplotlib.pyplot as plt
import pandas as pd



# DATAFILE
file_path = '../data/study2/data_2023_12_16.csv'

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



# AI TOTALS
tt = gpt3_ai_count + gpt3_human_count + gpt4_ai_count + gpt4_human_count + gptchat_ai_count + gptchat_human_count
tc = gpt3_ai_count + gpt4_ai_count + gptchat_ai_count
ai_correct =  tc / tt


# GPT 3
gpt3_correct = gpt3_ai_count / (gpt3_ai_count + gpt3_human_count)

# GPT3.5
gptchat_correct = gptchat_ai_count / (gptchat_ai_count + gptchat_human_count)


# GPT 4
gpt4_correct = gpt4_ai_count / (gpt4_ai_count + gpt4_human_count)

# Human
human_correct =  human_human_count / (human_human_count + human_ai_count)


# Define color palette
chosen_colors = ["#f7786b", "#034f84", "#034f84", "#034f84"]

# Data for the plot
models = ['Human', 'Davinci-3', 'GPT3.5-Turbo', 'GPT-4']
correct_rates = [human_correct * 100, gpt3_correct * 100, gptchat_correct * 100, gpt4_correct * 100]

# Create the bar plot using matplotlib
plt.figure(figsize=(8, 6))
bar_positions = range(len(models))  # Position of bars on x-axis

# Creating bars
bars = plt.bar(bar_positions, correct_rates, color=chosen_colors)

# Adding the title and labels
plt.title('Correctly Identified Source', fontweight='bold', fontsize=24, pad=24)
plt.xticks(bar_positions, models, fontsize=18)  # Set the position and labels of the ticks on the x-axis
plt.yticks([0, 25, 50, 75, 100], fontsize=20)
plt.ylim(0, 100)  # Set y-axis limit

# Draw a horizontal line at 50%
plt.axhline(y=50, color='black', linestyle='--')

# Add significance level text
x_position = 0  # X-coordinate for the "Human" bar
y_position = human_correct * 100 + 5  # Y-coordinate slightly above the bar
significance_level = "***"
plt.text(x_position, y_position + 5, significance_level, ha='center', fontsize=20)

# Display the percentages and total_n on top of the bars
for i, (rate, total) in enumerate(zip(correct_rates, total_n)):
    plt.text(i, rate + 1, f'{rate:.1f}%', ha='center', fontsize=22)
    plt.text(i, 3, f'N: {total}', ha='center', fontsize=16, color="white")

# Show the plot
plt.tight_layout()
plt.show()
