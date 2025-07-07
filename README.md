# Automated-Data-Quality-Rules-Engine-for-Transit-Violation-Logs

🧩 Problem Statement

Transit enforcement systems generate large volumes of violation data daily from bus lane cameras, GPS trackers, and field officers. These logs are mission-critical for enforcing traffic rules, reporting violations, and ensuring road safety. However, raw violation logs often suffer from poor data quality, such as:

Missing timestamps or location data

Duplicated violation records

Schema mismatches from upstream systems

Invalid geolocation values outside city boundaries

Without proper validation, these issues can lead to:

Misinformed decision-making

Legal or public trust concerns

Rejected reports by partner agencies

🌟 Objective

To develop a Python-based automated engine that performs daily quality checks on transit violation logs using rule-based validations. The engine will:

Detect schema mismatches

Identify duplicate violation records

Validate timestamp format and completeness

Check if geolocation values fall within acceptable geographic bounds

Output a daily data quality scorecard in CSV format

✅ What We Did

📁 Step 1: Loaded and Previewed the Dataset

Imported sample dataset sample_transit_violations.csv containing 100 records.

Fields include Violation_ID, Bus_ID, Timestamp, Latitude, Longitude, Violation_Type, and Road_Type.

Used Pandas to load and inspect the dataset.

🛠 Step 2: Defined and Executed Quality Checks

Implemented 4 rules:

Schema Check — Verified column names and order match the standard.

Duplicate Check — Counted duplicate Violation_IDs.

Timestamp Format Check — Used pd.to_datetime(..., errors='coerce') to detect invalid or missing timestamps.

Geofence Validation — Checked that all lat/lon values fall within the bounds of San Francisco.

📊 Step 3: Generated Daily Scorecard Report

Compiled all rule outputs into a DataFrame.

Wrote the results to data_quality_scorecard.csv

📀 Technologies Used

Python (Pandas, datetime)

Excel/CSV for scorecard reporting

✅ How to Run

Clone the repo or download the project files

Run data_quality_engine.py

Check output files: scorecard .csv/.xlsx
