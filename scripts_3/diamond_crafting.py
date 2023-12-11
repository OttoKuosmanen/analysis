import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = '../data/study3/data_2023_12_11.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Dropping unnecessary columns and rows
df = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)
df = df.drop([0, 1], axis=0)

# Chop columns to include only ratings
df = df.iloc[:, 22:-3]

# Convert ratings to integers and fill NaNs with zeros
df = df.applymap(lambda x: int(x) if str(x).isdigit() else 0)

# Define groups and scale points with corresponding suffixes
groups = ['Human', 'GPT3', 'GPT3.5', 'GPT4']
scale_points = {'Helpfulness': '1', 'Effectiveness': '2', 'Appropriateness': '3', 'Sensitivity': '4'}

# Aggregate data
aggregated_data = []
for group in groups:
    for scale_point, suffix in scale_points.items():
        # Columns for each group and scale point
        group_cols = [col for col in df.columns if col.startswith(group) and col.endswith(suffix)]
        
        if group_cols:
            # Average ratings for each scale point
            avg_ratings = df[group_cols].replace(0, np.nan).mean(axis=1)  # Replace 0 with NaN before averaging
            aggregated_data.append(pd.DataFrame({
                'Rating': avg_ratings,
                'Group': group,
                'ScalePoint': scale_point
            }))

# Combine into a single DataFrame and drop NaNs
df_aggregated = pd.concat(aggregated_data).dropna()

# Box Plot without Outliers
plt.figure(figsize=(12, 8))
sns.boxplot(x='Group', y='Rating', hue='ScalePoint', data=df_aggregated, palette='muted', showfliers=False)
plt.title('Aggregated Advice Quality Ratings by Source and Scale Point (Box Plot)')
plt.xlabel('Group')
plt.ylabel('Rating')
plt.legend(title='Scale Point')
plt.tight_layout()
plt.show()

# Violin Plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Group', y='Rating', hue='ScalePoint', data=df_aggregated, palette='muted', inner=None)
plt.title('Aggregated Advice Quality Ratings by Source and Scale Point (Violin Plot)')
plt.xlabel('Group')
plt.ylabel('Rating')
plt.legend(title='Scale Point')
plt.tight_layout()
plt.show()


