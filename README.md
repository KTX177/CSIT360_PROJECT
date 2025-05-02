# CSIT 360 - Final Project
## Brian Buckley, Mohammad Salem, Logan Li

Our project uses a dataset on gun violence incidents in the US, spanning January 2013 to March 2018. The data includes over 200,000 recorded incidents, compiled and scraped from [GunViolenceArchive.org](https://GunViolenceArchive.org).

Source: [https://www.kaggle.com/datasets/jameslko/gun-violence-data](https://www.kaggle.com/datasets/jameslko/gun-violence-data)

Drive Download: https://drive.google.com/drive/folders/1kKifAWcEK2YmSKhCu8LyMgTirKkU1fcj?usp=drive_link

### Dataset in a nutshell:

- Location (state, city/county, address, coordinates)
- Casualties (number killed/injured)
- Guns used (type, stolen status, number involved)
- Incident characteristics and participant details
- Congressional and legislative district info

### Dataset in depth:

- 29 Attributes 
- 239677 Rows/Incidents (a lot!)

| Column                    | Missing Values | % Missing |
|--------------------------|----------------|------------|
| `incident_id`            | 0              | -          |
| `date`                   | 0              | -          |
| `state`                  | 0              | -          |
| `city_or_county`         | 0              | -          |
| `address`                | 16,497         | ~6.9%      |
| `n_killed`               | 0              | -          |
| `n_injured`              | 0              | -          |
| `incident_url`           | 0              | -          |
| `incident_url_fields_missing`| 0          | -          |
| `source_url`             | 468            | ~0.2%      |
| `congressional_district` | 11,944         | ~5.0%      |
| `gun_stolen`             | 99,498         | ~41.5%     |
| `gun_type`               | 99,451         | ~41.5%     |
| `incident_characteristics`| 0             | -          |
| `latitude`               | 7,923          | ~3.3%      |
| `longitude`              | 7,923          | ~3.3%      |
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
| `sources`                | 0              | -          |
| `state_house_district`   | 38,772         | ~16.2%     |
| `state_senate_district`  | 32,335         | ~13.5%     |

### Pre-cleaning:

To get our raw CSV file onto GitHub, we used OpenRefine (a data cleaning tool by Google) to get our file size below GitHub's limit (100mb). The following columns were removed before being processed by any Python code:
- incident_url
- incident_url_fields_missing
- source_url
- sources

----------------------------------------------------------------------------------------------------------

## Project Goal

    Trends in gun violence over time (monthly, seasonal, and annual patterns)

    Most affected states or cities (TO-DO: or perhaps even congressional districts?)

    Common characteristics of high-casualty events (participant demographics/relationships)


## Feature Engineering

    Created new features (for example, total casualties = n_killed + n_injured)

    Extracted date features (year, month, weekday) for time series analysis

    Encoded categorical variables


## Modeling Approach

    Chosen models:
    Logistic regression & random forest to do multivariate & ensemble analyses respectively.

    We selected logistic regression over b/c it  models categorical outcomes like high-casualty events and regional trends (unlike linear regression which is, well, linear). Random forests were also chosen for their ability to capture non-linear relationships and interactions among features. A random forest ensemble may pick up on trends that other models fail to see - and our dataset is so large that overfitting isn't too much of a concern.

## Performance Metrics

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

## Key Findings

    Trends in gun violence over time (e.g., monthly/seasonal patterns)

    Most affected states or cities

    Common characteristics of high-casualty events

    Participant demographics and relationships
