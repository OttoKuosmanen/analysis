import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'data/study3/data_2023_12_8.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING

# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = data_ore.drop([0, 1], axis=0)

# Chop columns
ratings = data_ore.iloc[:, 22:-3]

# Step 1: Melt the DataFrame
melted_df = ratings.melt(var_name='Question_Model_Scale', value_name='Score')

# Step 2: Extract Question, Model, and Scale Information
melted_df[['Model', 'Question', 'Scale']] = melted_df['Question_Model_Scale'].str.split('_', expand=True)

# Step 3: Create a MultiIndex DataFrame without aggregation
# Create a MultiIndex from the columns 'Question', 'Model', and 'Scale'
melted_df.set_index(['Question', 'Model', 'Scale'], inplace=True)

# Display the final DataFrame
print(melted_df)
