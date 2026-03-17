import pandas as pd
import joblib

# Load saved objects
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# New input
new_data = pd.DataFrame([{
    "Distance_km": 5,
    "Weather": "Sunny",
    "Traffic_Level": "High",
    "Time_of_Day": "Evening",
    "Vehicle_Type": "Bike",
    "Preparation_Time_min": 15,
    "Courier_Experience_yrs": 2
}])

# Transform + predict
processed = preprocessor.transform(new_data)
prediction = model.predict(processed)

print(prediction[0])