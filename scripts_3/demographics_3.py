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
observations = sum(ratings['Non_NaN_Count'])

# Count rows with only NaN values (no answers)
count_all_nan = (ratings['Non_NaN_Count'] == 0).sum()
print(f"Participants with no answers: {count_all_nan}")

# Participant number

# Count the total number of participants
total_participants = data_ore.shape[0]
print(f"Total number of participants: {total_participants}")
participants_analysed = total_participants - count_all_nan
print(f"Analysed participants: {participants_analysed}")



# Observations

# Print total observations
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
