import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import joblib

# Load and clean data
df = pd.read_csv("dataset/Food_Delivery_Dataset.csv")
df = df.drop(columns=["Order_ID"]).dropna()

# Split features and target
X = df.drop(columns=["Delivery_Time_min"])
y = df["Delivery_Time_min"]

# Column groups
categorical_cols = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]
numerical_cols = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_cols)
    ],
    remainder="passthrough"
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Transform data
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and preprocessor
joblib.dump(model, "model.pkl")
joblib.dump(preprocessor, "preprocessor.pkl")