CSIT 360-01 
5/2/2025
Brian Buckley, Mohammad Salem, Logan Li 

Our project uses a comprehensive dataset on gun violence incidents in the United States, spanning from January 2013 to March 2018. The data includes over 260,000 recorded incidents, compiled and scraped from GunViolenceArchive.org, a non-profit dedicated to tracking gun-related incidents with accuracy and transparency.

Source: https://www.kaggle.com/datasets/jameslko/gun-violence-data

The dataset captures detailed information for each incident, including:

    Location (state, city/county, address, coordinates)

    Casualties (number killed/injured)

    Guns used (type, stolen status, number involved)

    Incident characteristics and participant details

    Congressional and legislative district info


About the Dataset:
- 29 Attributes 
- 239677 Rows/Incidents

| Column                    | Missing Values | % Missing |
|--------------------------|----------------|------------|
| `address`                | 16,497         | ~6.9%      |
| `source_url`             | 468            | ~0.2%      |
| `congressional_district` | 11,944         | ~5.0%      |
| `gun_stolen`             | 99,498         | ~41.5%     |
| `gun_type`               | 99,451         | ~41.5%     |
| `latitude` / `longitude` | 7,923          | ~3.3%      |
| `location_description`   | 197,588        | ~82.4%     |
| `n_guns_involved`        | 99,451         | ~41.5%     |
| `notes`                  | 81,017         | ~33.8%     |
| `participant_age`        | 92,298         | ~38.5%     |
| `participant_age_group`  | 42,119         | ~17.6%     |
| `participant_gender`     | 36,362         | ~15.2%     |
| `participant_name`       | 122,253        | ~51.0%     |
| `participant_relationship`| 223,903       | ~93.4%     |
| `participant_status`     | 27,626         | ~11.5%     |
| `participant_type`       | 24,863         | ~10.4%     |
| `state_house_district`   | 38,772         | ~16.2%     |
| `state_senate_district`  | 32,335         | ~13.5%     |

----------------------------------------------------------------------------------------------------------

Feature Engineering

    Created new features (e.g., total casualties = n_killed + n_injured)

    Extracted date features (year, month, weekday) for time series analysis

    Encoded categorical variables (e.g., state, gun type)

    Aggregated participant details for simplified modeling

Modeling Approach GENERATED FROM CHAT GPT

    Chosen model(s):
    (e.g., Decision Tree, Random Forest, Logistic Regression, XGBoost)

    Reason for choice:

        Handles categorical/numerical features well

        Easy to interpret (especially Decision Trees)

        Performs well with imbalanced or sparse data

Performance Metrics Generated from CHATGPT

    Metrics used:

        Accuracy, Precision, Recall, F1-score

        Confusion Matrix

        AUC-ROC (if applicable)

    Model evaluation results:
    (Insert table or summary of performance)

        Example:

            Accuracy: 92.3%

            F1 Score: 0.88

            AUC: 0.94

Key Findings Generated from CHATGPT

    Trends in gun violence over time (e.g., monthly/seasonal patterns)

    Most affected states or cities

    Common characteristics of high-casualty events

    Participant demographics and relationships