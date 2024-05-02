import pandas as pd

# DATAFILE
file_path = '../data/study3/data_2023_12_16.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# CHIPPING
# Remove Columns
data_ore = df.drop(["StartDate", "EndDate", "Status", "ResponseId", "UserLanguage"], axis=1)

# Remove Rows
data_ore = data_ore.drop([0, 1], axis=0)

# Chop columns to include only ratings
ratings_only = data_ore.iloc[:, 17:-3]
ratings = ratings_only.copy()

# Count non-NaN values per row
ratings['Non_NaN_Count'] = ratings.apply(lambda row: row.notnull().sum(), axis=1)


# Count rows with only NaN values (no answers)
count_all_nan = (ratings['Non_NaN_Count'] == 0).sum()
print(f"Participants with no answers: {count_all_nan}")

# Count rows with partial nan values
count_partial = ((ratings['Non_NaN_Count'] != 0) & (ratings['Non_NaN_Count'] != 24)).sum()
print ("Partial completion:", count_partial)


# Count rows with full completion
count_full = (ratings['Non_NaN_Count'] == 24).sum()
print ("Full completion:", count_full)


# Count the total number of participants
total_participants = count_all_nan + count_full + count_partial
print(f"Total number of participants: {total_participants}")
participants_analysed = count_full + count_partial
print(f"Analysed participants: {participants_analysed}")


# Print total observations
observations = sum(ratings['Non_NaN_Count'])
print(f"Total observations: {observations}")


# Age
print("Age")
ratings['Age'] = data_ore['Age']
analysed = ratings[ratings['Non_NaN_Count'] > 0]
age_analysis = analysed['Age'].value_counts()
print("\nAge distribution for partial participation:")
print(age_analysis)

#Gender
print("Gender")
ratings['Gender'] = data_ore['Gender']
analysed = ratings[ratings['Non_NaN_Count'] > 0]
gender_analysis = analysed['Gender'].value_counts()
print("\nGender distribution for partial participation:")
print(gender_analysis)

# Education
print("Education")
ratings['Education'] = data_ore['Education']
analysed = ratings[ratings['Non_NaN_Count'] > 0]
education_analysis = analysed['Education'].value_counts()
print("\nEducation distribution for partial participation:")
print(education_analysis)

# Location
print("Location")
ratings['Country'] = data_ore['Country']
ratings['Country_TEXT'] = data_ore['Country_9_TEXT']
analysed = ratings[ratings['Non_NaN_Count'] > 0].copy()
analysed['Country'] = analysed.apply(
    lambda row: row['Country_TEXT'] if row['Country'] == 'Other (Specify Below)' else row['Country'], 
    axis=1
)
location_analysis = analysed['Country'].value_counts()
print("\nLocation distribution for partial participation:")
print(location_analysis)
print(sum(location_analysis))

# Source
print("Source")
ratings['Source'] = data_ore['Source']
analysed = ratings[ratings['Non_NaN_Count'] > 0]
source_analysis = analysed['Source'].value_counts()
print("\nSource distribution for partial participation:")
print(source_analysis)

# CALUCULATIONS of EXPERIMENTAL TIME

# Section data for average time
exe_time = data_ore.iloc[:, [0,1,5]]

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
