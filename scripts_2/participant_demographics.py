import pandas as pd

def count_values_in_row(row, value_to_count, misspelled_value=None):
    return ((row == value_to_count) | (row == misspelled_value)).sum()

# DATAFILE
file_path = '../data/study2/data_2023_12_16.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = df.drop([0, 1], axis=0)

# Chop columns to include only participant information
intel = data_ore.iloc[:, 5:-1]


# Chop columns to include only ratings
ratings_only = data_ore.iloc[:, 22:-2]
ratings = ratings_only.copy()


# Run counter for observations and add a total count column
for index, row in ratings.iterrows():
    human_count = count_values_in_row(row, 'Human', 'Human Answer')
    ai_count = count_values_in_row(row, 'AI')
    ratings.loc[index, 'Human'] = human_count
    ratings.loc[index, 'AI'] = ai_count
    ratings.loc[index, 'Total_Count'] = human_count + ai_count

# Sum up all observations for 'Human' and 'AI'
total_count_human = ratings['Human'].sum()
total_count_AI = ratings['AI'].sum()

observations = int(total_count_AI + total_count_human)
print(f"Observations: {observations}")

# Count rows with 0 answers
count_zero_answers = (ratings['Total_Count'] == 0).sum()
print(f"Participants with 0 answers: {count_zero_answers}")

# Count rows with answers more than 0 but less than 6
count_partial_answers = ((ratings['Total_Count'] > 0) & (ratings['Total_Count'] < 9)).sum()
print(f"Participants with partial completion (more than 0 but less than 6): {count_partial_answers}")

# Count rows with 6 answers
count_full_answers = (ratings['Total_Count'] == 9).sum()
print(f"Participants with full completion: {count_full_answers}")


participants = count_full_answers + count_partial_answers + count_zero_answers
print("Participants:", participants)

participants_in_analysis = participants - count_zero_answers
print(f"participants_in_analysis: {participants_in_analysis}")

# Gender
print("GENDER ")

# Add the Gender column to the ratings DataFrame
ratings['gender'] = data_ore['gender']

# Filter for complete and partial participation
analysed = ratings[ratings['Total_Count'] > 0]


# Gender distribution for partial participation
gender_analysis = analysed['gender'].value_counts()
print("\nGender distribution for partial participation:")
print(gender_analysis)

# Age
print("age")

# Add the Age column to the ratings DataFrame
ratings['age'] = data_ore['age']

# Filter for complete and partial participation
analysed = ratings[ratings['Total_Count'] > 0]


# Age distribution for partial participation
age_analysis = analysed['age'].value_counts()
print("\nAge distribution for partial participation:")
print(age_analysis)


# Education
print("education ")

# Add the Education column to the ratings DataFrame
ratings['education'] = data_ore['education']

# Filter for complete and partial participation
analysed = ratings[ratings['Total_Count'] > 0]


# Education distribution for partial participation
education_analysis = analysed['education'].value_counts()
print("\nEducation distribution for partial participation:")
print(education_analysis)
 
# Location
print("location")

# Add the Contry column to the ratings DataFrame
ratings['Country'] = data_ore['Country']
ratings['Country_TEXT'] = data_ore['Country_9_TEXT']

# Filter for complete and partial participation
analysed = ratings[ratings['Total_Count'] > 0].copy()

# Replace 'other'
analysed['Country'] = analysed.apply(
    lambda row: row['Country_TEXT'] if row['Country'] == 'Other (Specify Below)' else row['Country'], 
    axis=1
)

# Country distribution for partial participation
location_analysis = analysed['Country'].value_counts()
print("\nLocation distribution for partial participation:")
print(location_analysis)

print(sum(location_analysis))



# Source
print("Source")

# Add the Country column to the ratings DataFrame
ratings['source'] = data_ore['source']

# Filter for complete and partial participation
analysed = ratings[ratings['Total_Count'] > 0]

# Country distribution for partial participation
source_analysis = analysed['source'].value_counts()
print("\nSource distribution for partial participation:")
print(source_analysis)

# CALUCULATIONS of EXPERIMENTAL TIME

# Section data for average time
exe_time = data_ore.iloc[:, [3,4,10]]

# Filter the DataFrame Progress should be 100 and participant agreed to participate.
completed = exe_time[(exe_time['Progress'] == '100') & (exe_time['Consent'] == "I agree to participate -- Take me to the questionnaire!")].copy()

# Duration was stored in a string variable, transform to numeric.
completed['Duration (in seconds)'] = pd.to_numeric(completed['Duration (in seconds)'], errors='coerce')

#Filter out participants that took brakes
completed_filtered = completed[completed['Duration (in seconds)'] <= 7200]

# Calculate the average of Duration
print("Average time in minutes")
average_time = completed['Duration (in seconds)'].mean()
average_minutes = average_time / 60
print(average_minutes)

# Calculate the average of Duration when excluding participants that took more than 2 hours
print("Average time in minutes: with participants that took less than 2 hours to complete")
average_time_filtered = completed_filtered['Duration (in seconds)'].mean()
average_minutes_filtered = average_time_filtered / 60
print(average_minutes_filtered)



 

