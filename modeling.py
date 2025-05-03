# modeling.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Aside from the Random Forest, we

#Fatal vs. Non-Fatal Classification (Binary)

# Theory: This could help identify the likelihood of an incident leading to a fatality. It’s a crucial target for public safety initiatives, as understanding which incidents are more likely to result in deaths can guide policy decisions, law enforcement, and medical responses.
# Script goal to predict whether the incident is likely to be fatal or not.
# -> Target variable: target = (df['n_killed'] > 0).astype(int) (If > 1 killed, then FATAL)
# -> Outcome: 0 (Non-Fatal), 1 (Fatal)
# -> Use case: Public health organizations can possibly focus efforts on preventing more fatal gun violence, which features 
# Can potentially help understand risk factors for fatal incidents, explore patterns by location, gender, or age group
# ----------------------------------------------------CODE------------------------------------------------------------------

# 1. Load cleaned data
df = pd.read_csv('data/cleaned_gun_violence_data.csv')  # Adjust filename as needed
# 2. Creation of target variable for this case
df['fatalities_occurred'] = (df['n_killed'] > 0).astype(int)
print(df)
# 3. Select features
features = [
    'n_injured',
    'n_guns_involved',
    'state',
    'city_or_county',
    'participant_age_group',
    'participant_gender'
]

X = df[features]
y = df['fatalities_occurred']

# 4. Preprocessing for categorical variables
categorical_features = ['state', 'city_or_county', 'participant_age_group', 'participant_gender']
numerical_features = ['n_injured', 'n_guns_involved']

# Preprocessing pipeline
preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ('num', SimpleImputer(strategy='mean'), numerical_features)
])

# 5. Create model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# 6. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Train model
model.fit(X_train, y_train)

# 8. Evaluate
y_pred = model.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
