import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# DATAFILE
file_path = '../data/study1/data_2023_12_9.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 22:-2]


 #read comments
for comment in df['Comment']:
    print(comment)



# Problem Human answer ! Human instance 1

# Group ratings

GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]


# Count "Human" and "AI" for each group

gpt3_human_count = (GPT3 == 'Human').sum().sum()
gpt3_ai_count = (GPT3 == 'AI').sum().sum()
g3 = int(gpt3_ai_count)

gptchat_human_count = (GPTchat == 'Human').sum().sum()
gptchat_ai_count = (GPTchat == 'AI').sum().sum()
gc = int(gptchat_ai_count)

gpt4_human_count = (GPT4 == 'Human').sum().sum()
gpt4_ai_count = (GPT4 == 'AI').sum().sum()
g4 = int(gpt4_ai_count)

# comparison
human_chosen = gpt3_human_count + gpt4_human_count + gptchat_human_count
ai_chosen = gpt3_ai_count + gpt4_ai_count + gptchat_ai_count

total = human_chosen + ai_chosen

print(f"Human chosen: {human_chosen} times")

print(f"AI chosen: {ai_chosen} times")


print(f"Human chosen: {human_chosen/total}%")
print(f"AI chosen: {ai_chosen/total}%")



# Define the model names and their respective percentages
models = ['GPT3', 'GPT3.5', 'GPT4']
percentages = [g3, gc, g4]  # Replace these with actual values

# Create an array with the position of each bar along the x-axis
x_pos = np.arange(len(models))

# Set up the bar chart
plt.figure(figsize=(10, 6))

# Use Seaborn's colorblind color palette
colors_blind = sns.color_palette('colorblind')

# Assign colors from the palette to the bars
bars = plt.bar(x_pos, percentages, capsize=6, color=colors_blind[:3])

# Add the data value on head of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval,1), ha='center', va='bottom', color='black')

# Set the x-axis labels horizontally
plt.xticks(x_pos, models)

# Set labels and title with bold font
plt.ylabel('% Frequency that model advice is preferred over best Reddit advice', fontsize=10)
plt.xlabel('Model', fontsize=12)
plt.title('Comparison of Model Advice Preference', fontsize=16, fontweight='bold')

# Set the y-axis range to 0-100%
plt.ylim(0, 100)

# Adding a horizontal line at 50% frequency
plt.axhline(y=50, color='black', linestyle='--')

# Show the figure
plt.tight_layout()
plt.show()


