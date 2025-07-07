import pandas as pd
from datetime import datetime
df = pd.read_csv("sample_transit_violations.csv")
print(df.head())
print()

# Show column names
print(df.columns.tolist())

# Definining the expected schema:
expected_columns = [
    "Violation_ID", "Bus_ID", "Timestamp",
    "Latitude", "Longitude", "Violation_Type", "Road_Type"
]


### 1st Check: Schema check.
def check_schema(df, expected_columns):
    actual_columns = list(df.columns)
    return actual_columns == expected_columns

### 2nd Check: Duplicate Violation_ID check and return the count.
def check_duplicates(df):
    return df["Violation_ID"].duplicated().sum()

### 3rd Check: Timestampp validation
def check_timestamp_format(df):
    invalid_count = 0
    for ts in df["Timestamp"]:
        if pd.isna(ts):
            invalid_count += 1
            continue
        try:
            datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        except Exception:
            invalid_count += 1
    return invalid_count


### 4th Check: Geofencing Check
def check_geofence(df):
    invalid_lat = df[(df["Latitude"] < 37.70) | (df["Latitude"] > 37.85)]
    invalid_lon = df[(df["Longitude"] < -122.52) | (df["Longitude"] > -122.35)]
    return len(invalid_lat) + len(invalid_lon)

### Scorecard dictionary to keep the track of counts
scorecard = {
    "Schema_Valid": check_schema(df, expected_columns),
    "Duplicate_IDs": check_duplicates(df),
    "Invalid_Timestamps": check_timestamp_format(df),
    "Out_of_Bounds_Locations": check_geofence(df)
}

print()

print(scorecard)

# Display scorecard
print("\n📋 Data Quality Scorecard:")
for rule, result in scorecard.items():
     if result is True or result == 0:
        print(f"{rule}: ✅ Passed")
     else:
        print(f"{rule}: ❌ {result} issue(s)")
    
    
### Generate daily scorecard CSV file:

# converting the dictionary into a dataframe
scorecard_df = pd.DataFrame([scorecard])

# save the dataframe as a CSV file:
scorecard_df.to_csv("daily_data_quality_scorecard.csv", index=False)
