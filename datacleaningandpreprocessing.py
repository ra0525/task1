import pandas as pd

# Load the dataset
df = pd.read_csv("KaggleV2-May-2016.csv")

# --- Initial Inspection ---
print("Initial Shape:", df.shape)
print("Initial Nulls:\n", df.isnull().sum())
print("Initial Columns:", df.columns.tolist())

# --- Step 1: Rename Columns ---
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace('-', '_')
    .str.replace(' ', '_')
)
df.rename(columns={'handcap': 'handicap'}, inplace=True)

# --- Step 2: Remove Duplicates ---
duplicates_count = df.duplicated().sum()
df.drop_duplicates(inplace=True)

# --- Step 3: Handle Missing Values ---
# (No nulls in this dataset but it's good to check)
nulls_after = df.isnull().sum()

# --- Step 4: Standardize Categorical Columns ---
df['gender'] = df['gender'].str.upper()
df['no_show'] = df['no_show'].str.strip().str.lower().replace({'yes': 'no_show', 'no': 'show'})

# --- Step 5: Convert Dates to Datetime ---
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

# --- Step 6: Validate Data Types ---
# Remove rows where 'age' is negative
df = df[df['age'] >= 0]

# --- Final Dataset Info ---
print("Final Shape:", df.shape)
print("Nulls After Cleaning:\n", df.isnull().sum())

# --- Save Cleaned Dataset ---
df.to_csv("cleaned_medical_appointments.csv", index=False)
print("✅ Cleaned dataset saved as 'cleaned_medical_appointments.csv'")

# --- Optional: Summary Output ---
summary = {
    "Initial Rows": 110527,
    "Final Rows": df.shape[0],
    "Duplicates Removed": duplicates_count,
    "Nulls After Cleaning": nulls_after.to_dict(),
    "Renamed Columns": df.columns.tolist(),
    "Standardized Columns": ["gender", "no_show"],
    "Date Columns Converted": ["scheduledday", "appointmentday"],
    "Negative Ages Removed": True
}

print("\n--- Summary of Cleaning ---")
for key, value in summary.items():
    print(f"{key}: {value}")
