import pandas as pd
import numpy as np

def load_data(filepath):

    # Load data from CSV in data folder
    df = pd.read_csv(filepath, low_memory=False)
    print(f"Shape: {df.shape}")
    return df

# Checking to see basic details and stats
def inspect_data(df):
    print("\n--- Data Info ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isna().sum().sort_values(ascending=False))
    print("\n--- Sample Rows ---")
    print(df.head())

# Drop high-missing cols - we may need to drop more later
def drop_columns(df):
    
    #Drop columns with too many missing values or irrelevant info.
    columns_to_drop = [
        'participant_relationship', 
        'location_description', 
        'participant_name',
        'notes'
    ]
    df = df.drop(columns=columns_to_drop, errors='ignore')
    return df

# Handle other missing vals
def impute_missing(df):

    # Fill mode for categorical
    df['gun_stolen'] = df['gun_stolen'].fillna('Unknown')
    df['gun_type'] = df['gun_type'].fillna('Unknown')

    # Fill numeric with 0
    df['n_guns_involved'] = df['n_guns_involved'].fillna(0)

    # Drop rows missing coords.
    df = df.dropna(subset=['latitude', 'longitude'])

    return df

# Feat. engineering
def feature_engineering(df):
    
    # Creating some new features for later use (plots/modeling)
    df['total_victims'] = df['n_killed'] + df['n_injured']
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.day_name()
    return df

# Save cleaned data
def save_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

# MAIN FUNCTION
# We run through all the other functs. above essentially in order of appearance

if __name__ == "__main__":
    input_csv = './data/raw_gun_violence_data.csv'
    output_csv = './data/cleaned_gun_violence_data.csv'

    df_raw = load_data(input_csv)
    inspect_data(df_raw)

    df_clean = drop_columns(df_raw)
    df_clean = impute_missing(df_clean)
    df_clean = feature_engineering(df_clean)

    save_data(df_clean, output_csv)
