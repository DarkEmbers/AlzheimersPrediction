import pandas as pd

df = pd.read_csv("../Data/alzheimer.csv")

# Check for out-of-range values for Age (between 60 and 98)
age_outliers = df[(df['Age'] < 60) | (df['Age'] > 98)]

# Check for out-of-range values for EDUC (between 0 and 23 years)
educ_outliers = df[(df['EDUC'] < 0) | (df['EDUC'] > 23)]

# Check for out-of-range values for MMSE (between 0 and 30, as MMSE scores range between 0 and 30)
mmse_outliers = df[(df['MMSE'] < 0) | (df['MMSE'] > 30)]

# Check for out-of-range values for SES (Socioeconomic status is often between 1 and 5, adjust as per your data)
ses_outliers = df[(df['SES'] < 1) | (df['SES'] > 5)]

# Check for out-of-range values for CDR (Clinical Dementia Rating, values are typically between 0 and 3)
cdr_outliers = df[(df['CDR'] < 0) | (df['CDR'] > 3)]

# Check for unexpected values in categorical columns
unexpected_group_values = df[~df['Group'].isin(['Demented', 'Nondemented'])]
unexpected_gender_values = df[~df['M/F'].isin(['M', 'F'])]

# Verify no outliers or unexpected values
if (age_outliers.empty and educ_outliers.empty and mmse_outliers.empty and ses_outliers.empty and 
    cdr_outliers.empty and unexpected_group_values.empty and unexpected_gender_values.empty):
    print("No garbage values found in the dataset.")
else:
    print("Garbage values detected.")
    
    if not age_outliers.empty:
        print("\n--- Age outliers ---")
        print(age_outliers)
    
    if not educ_outliers.empty:
        print("\n--- Education outliers ---")
        print(educ_outliers)
    
    if not mmse_outliers.empty:
        print("\n--- MMSE outliers ---")
        print(mmse_outliers)

    if not ses_outliers.empty:
        print("\n--- SES outliers ---")
        print(ses_outliers)
    
    if not cdr_outliers.empty:
        print("\n--- CDR outliers ---")
        print(cdr_outliers)
    
    if not unexpected_group_values.empty:
        print("\n--- Unexpected values in Group ---")
        print(unexpected_group_values)
    
    if not unexpected_gender_values.empty:
        print("\n--- Unexpected values in Gender ---")
        print(unexpected_gender_values)

# Count the number of missing values per column
missing_values_per_column = df.isnull().sum()
print("Missing values per column:")
print(missing_values_per_column)

# Remove rows with any missing values
df = df.dropna()
df = df[df['Group'] != 'Converted']

# Convert group to numerical values
df["Group"] = df["Group"].map({"Nondemented": 0, "Demented": 1, "Converted": 2})

# Convert gender to numerical values
df["M/F"] = df["M/F"].map({"M": 0, "F": 1})

# save the cleaned data to a new csv file
df.to_csv('../Data/cleaned_alzheimer.csv', index=False)