import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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



#Base statistics
mean_h = np.mean(data_Human)
mean_3 = np.mean(data_GPT3)
mean_chat = np.mean(data_GPTchat)
mean_4 = np.mean(data_GPT4)


mead_h = np.median(data_Human)
mead_3 = np.median(data_GPT3)
mead_chat = np.median(data_GPTchat)
mead_4 = np.median(data_GPT4)


sd_h = np.std(data_Human) 
sd_3 = np.std(data_GPT3)
sd_chat = np.std(data_GPTchat)
sd_4 = np.std(data_GPT4)


#statistics for all scale points for the Human group
mean_h_helpfulness = np.mean(data_human_helpfulness)
mean_h_effectiveness = np.mean(data_human_effectiveness)
mean_h_appropriateness = np.mean(data_human_appropriateness)
mean_h_sensitivity = np.mean(data_human_sensitivity)

median_h_helpfulness = np.median(data_human_helpfulness)
median_h_effectiveness = np.median(data_human_effectiveness)
median_h_appropriateness = np.median(data_human_appropriateness)
median_h_sensitivity = np.median(data_human_sensitivity)



#statistics for all scale points for the GPT3 group
mean_3_helpfulness = np.mean(data_GPT3_helpfulness)
mean_3_effectiveness = np.mean(data_GPT3_effectiveness)
mean_3_appropriateness = np.mean(data_GPT3_appropriateness)
mean_3_sensitivity = np.mean(data_GPT3_sensitivity)

median_3_helpfulness = np.median(data_GPT3_helpfulness)
median_3_effectiveness = np.median(data_GPT3_effectiveness)
median_3_appropriateness = np.median(data_GPT3_appropriateness)
median_3_sensitivity = np.median(data_GPT3_sensitivity)



#statistics for all scale points for the GPTchat group
mean_chat_helpfulness = np.mean(data_GPTchat_helpfulness)
mean_chat_effectiveness = np.mean(data_GPTchat_effectiveness)
mean_chat_appropriateness = np.mean(data_GPTchat_appropriateness)
mean_chat_sensitivity = np.mean(data_GPTchat_sensitivity)

median_chat_helpfulness = np.median(data_GPTchat_helpfulness)
median_chat_effectiveness = np.median(data_GPTchat_effectiveness)
median_chat_appropriateness = np.median(data_GPTchat_appropriateness)
median_chat_sensitivity = np.median(data_GPTchat_sensitivity)



#statistics for all scale points for the GPT4 group
mean_4_helpfulness = np.mean(data_GPT4_helpfulness)
mean_4_effectiveness = np.mean(data_GPT4_effectiveness)
mean_4_appropriateness = np.mean(data_GPT4_appropriateness)
mean_4_sensitivity = np.mean(data_GPT4_sensitivity)

median_4_helpfulness = np.median(data_GPT4_helpfulness)
median_4_effectiveness = np.median(data_GPT4_effectiveness)
median_4_appropriateness = np.median(data_GPT4_appropriateness)
median_4_sensitivity = np.median(data_GPT4_sensitivity)

## PLOTTING
 
# Data
groups = ['Human', 'GPT-3', 'GPT-3.5', 'GPT-4']
scale_points = ['Helpfulness', 'Effectiveness', 'Appropriateness', 'Sensitivity']

# A color palette with distinguishable and colorblind-friendly colors
color_palette = sns.color_palette("colorblind")
chosen_colors = [2,8,9,6]

# Means for each group and scale point
means = [
    [mean_h_helpfulness, mean_h_effectiveness, mean_h_appropriateness, mean_h_sensitivity],
    [mean_3_helpfulness, mean_3_effectiveness, mean_3_appropriateness, mean_3_sensitivity],
    [mean_chat_helpfulness, mean_chat_effectiveness, mean_chat_appropriateness, mean_chat_sensitivity],
    [mean_4_helpfulness, mean_4_effectiveness, mean_4_appropriateness, mean_4_sensitivity]
]
# FONTS

# Define a dictionary for font properties
title_font = {
    'fontsize': 22,  # Adjust the font size as needed
    'fontweight': 'bold',  # Make the title bold
    'fontfamily': 'serif',  # Change the font family if desired
}


# Set the width of the bars
bar_width = 0.20

# Create positions for the bars
x = np.arange(len(scale_points))
x_labels = groups
 
# Create subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Create bars for each scale point
for i, scale_point in enumerate(scale_points):
    ax.bar(x + i * bar_width, [group_means[i] for group_means in means], bar_width, label=scale_point,color=color_palette[chosen_colors[i]])

# Add a horizontal line for the total mean for each group
ax.axhline(mean_h, color='black', linestyle='--', xmin=0.048, xmax = 0.048 * 5 - 0.005)
ax.axhline(mean_3, color='black', linestyle='--', xmin=0.048 * 6 - 0.002, xmax = 0.048 * 10 - 0.005)
ax.axhline(mean_chat, color='black', linestyle='--', xmin=0.048 * 11 - 0.005, xmax = 0.048 * 15 - 0.005)
ax.axhline(mean_4, color='black', linestyle='--', xmin=0.048 * 16 - 0.005, xmax = 0.048 * 20 - 0.005)

# Add numbers to the lines
ax.text(0.30, mean_h, f'{mean_h:.2f}', color='black', fontsize=15, ha='center', va='bottom', fontweight='bold')
ax.text(1.30, mean_3, f'{mean_3:.2f}', color='black', fontsize=15, ha='center', va='bottom',fontweight='bold')
ax.text(2.30, mean_chat, f'{mean_chat:.2f}', color='black', fontsize=15, ha='center', va='bottom',fontweight='bold')
ax.text(3.30, mean_4, f'{mean_4:.2f}', color='black', fontsize=15, va='bottom',fontweight='bold', ha='center')




# Set labels, title, and ticks
ax.set_ylabel('Means', fontdict=title_font)
ax.set_title('Advice Quality Ratings by Source', fontdict=title_font)
ax.set_xticks(x + (bar_width * (len(groups) - 1)) / 2)
ax.set_xticklabels(x_labels, fontdict=title_font)
ax.legend(fontsize=15,framealpha=0.8)

ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='x', labelsize=16)
# Get the handles and labels from the original legend
handles, labels = ax.get_legend_handles_labels()

# Add your custom legend item to the handles and labels
custom_legend_item = plt.Line2D([0], [0], color='black', linestyle='--', lw=2, label='Group means')
handles.append(custom_legend_item)
labels.append('Group mean')

# Remove the original legend
ax.get_legend().remove()

# Add the combined legend with both original and custom items
ax.legend(handles, labels, fontsize=12, title_fontsize=14, framealpha=0.8)



# Show the plot
plt.tight_layout()
plt.show()

