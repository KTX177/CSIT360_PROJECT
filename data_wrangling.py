# data_wrangling.py

import pandas as pd
import numpy as np

# ----------------------
# 1. Load Dataset
# ----------------------
def load_data(filepath):
    """Load gun violence dataset from CSV."""
    df = pd.read_csv(filepath, encoding='ISO-8859-1', low_memory=False)
    print(f"Data loaded. Shape: {df.shape}")
    return df


# ----------------------
# 2. Initial Inspection
# ----------------------
def inspect_data(df):
    """Print basic info and missing value stats."""
    print("\n--- Data Info ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isna().sum().sort_values(ascending=False))
    print("\n--- Sample Rows ---")
    print(df.head())


# ----------------------
# 3. Drop High-Missing Columns
# ----------------------
def drop_columns(df):
    """Drop columns with too many missing values or irrelevant info."""
    columns_to_drop = [
        'participant_relationship', 
        'location_description', 
        'participant_name',
        'notes'
    ]
    df = df.drop(columns=columns_to_drop, errors='ignore')
    return df


# ----------------------
# 4. Handle Missing Values
# ----------------------
def impute_missing(df):
    """Fill missing values where appropriate."""
    # Fill mode for categorical
    df['gun_stolen'] = df['gun_stolen'].fillna('Unknown')
    df['gun_type'] = df['gun_type'].fillna('Unknown')

    # Fill numeric with 0 if reasonable
    df['n_guns_involved'] = df['n_guns_involved'].fillna(0)

    # Drop rows missing location coordinates
    df = df.dropna(subset=['latitude', 'longitude'])

    return df


# ----------------------
# 5. Feature Engineering
# ----------------------
def feature_engineering(df):
    """Create new useful features."""
    df['total_victims'] = df['n_killed'] + df['n_injured']
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.day_name()
    return df


# ----------------------
# 6. Save Cleaned Data
# ----------------------
def save_data(df, output_path):
    """Save the cleaned DataFrame to a new CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")


# ----------------------
# Main Execution Block
# ----------------------
if __name__ == "__main__":
    input_csv = 'gun-violence-data_01-2013_03-2018.csv'
    output_csv = 'cleaned_gun_violence_data.csv'

    df_raw = load_data(input_csv)
    inspect_data(df_raw)

    df_clean = drop_columns(df_raw)
    df_clean = impute_missing(df_clean)
    df_clean = feature_engineering(df_clean)

    save_data(df_clean, output_csv)
