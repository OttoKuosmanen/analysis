import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Patch
import matplotlib.ticker as mtick

# DATAFILE
file_path = '../data/study1/data_2023_12_11.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings = data_ore.iloc[:, 22:-2]

"""
 #read comments
for comment in df['Comment']:
    print(comment)
"""

"""
# Problem Human answer ! Human instance 1
"""

# Group ratings

GPT3 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3_')]]
GPTchat = ratings[[col for col in ratings.columns if col.lower().startswith('gpt3.5')]]
GPT4 = ratings[[col for col in ratings.columns if col.lower().startswith('gpt4')]]


# Count "Human" and "AI" for each group

gpt3_human_count = (GPT3 == 'Human').sum().sum()
gpt3_ai_count = (GPT3 == 'AI').sum().sum()
g3 = int(gpt3_ai_count)
gpt3_total_count = gpt3_human_count + gpt3_ai_count

gptchat_human_count = (GPTchat == 'Human').sum().sum()
gptchat_ai_count = (GPTchat == 'AI').sum().sum()
gc = int(gptchat_ai_count)
gptchat_total_count = gptchat_human_count + gptchat_ai_count

gpt4_human_count = (GPT4 == 'Human').sum().sum()
gpt4_ai_count = (GPT4 == 'AI').sum().sum()
g4 = int(gpt4_ai_count)
gpt4_total_count = gpt4_human_count + gpt4_ai_count

n = [gpt3_total_count, gptchat_total_count, gpt4_total_count]
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
percentages = [g3, gc, g4]

# Reminders = human chosen.
complement_percentages = [100 - p for p in percentages]

# Create an array with the position of each bar along the x-axis
x_pos = np.arange(len(models))

# Set up the bar chart
plt.figure(figsize=(10, 6),facecolor="silver")



# Use Seaborn's colorblind color palette
colors_blind = sns.color_palette('colorblind')

# Assign colors from the palette to the bars
ai_bars = plt.bar(x_pos, percentages, color='steelblue', label='AI Chosen', width=0.66)

# Creating the complement bars and adding complement data labels
for i in range(len(models)):
    complement_bar = plt.bar(x_pos[i], complement_percentages[i], bottom=percentages[i], 
                             color='salmon', edgecolor='none', label='Human Chosen' if i == 0 else "", width =0.66)
    # Calculate the position for the complement label
    label_position = percentages[i] + 4 
    plt.text(x_pos[i], label_position, f"{round(complement_percentages[i],1)}%", 
             ha='center', va='center', color='white', fontweight='bold')

# Adding data labels
for bar, percentage, number in zip(ai_bars, percentages, n):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 4, f"{round(percentage,1)}%", 
             ha='center', va='center', color='black', fontweight='bold')
    
    # Label for the number at the bottom of the bar
    plt.text(bar.get_x() + bar.get_width()/2, 25, f"N={str(number)}", 
             ha='center', va='bottom', color='black', fontweight='bold')

# Create custom handles for the legend
legend_handles = [
    Patch(facecolor='salmon', label='Human Chosen'),
    Patch(facecolor='steelblue', label='AI Chosen')
]

# Add a legend with custom order and move it outside the plot area
plt.legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(0.8, 1))

# Adjust the subplot margins to provide more space
plt.subplots_adjust(right=0.75)

# Set the x-axis labels horizontally
plt.xticks(x_pos, models, fontweight='bold')

plt.ylabel('Precentage of Choosing Advice as More Helpful by Source', fontsize=10, fontweight='bold')
plt.xlabel('Model', fontsize=12, fontweight='bold')
plt.title('What Advice is More Helpful: Percentage Distribution of Choice', fontsize=16, fontweight='bold')

# Set the y-axis range to 0-100%
plt.ylim(0, 100,)
plt.yticks([0, 25, 50, 75, 100])
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(100))

# Adding a horizontal line at 50% frequency
plt.axhline(y=50, color='black', linestyle='--')

# Show the figure
plt.tight_layout()
plt.show()


