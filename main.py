from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib


# Load saved model and preprocessor
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")


app = FastAPI(title="Delivery Time Prediction API")


# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DeliveryInput(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: float
    Courier_Experience_yrs: float


@app.get("/")
def home():
    return {
        "message": "Delivery Time Prediction API is running"
    }


@app.post("/predict")
def predict_delivery_time(data: DeliveryInput):
    try:
        input_data = pd.DataFrame([{
            "Distance_km": data.Distance_km,
            "Weather": data.Weather,
            "Traffic_Level": data.Traffic_Level,
            "Time_of_Day": data.Time_of_Day,
            "Vehicle_Type": data.Vehicle_Type,
            "Preparation_Time_min": data.Preparation_Time_min,
            "Courier_Experience_yrs": data.Courier_Experience_yrs
        }])

        processed_data = preprocessor.transform(input_data)
        prediction = model.predict(processed_data)

        return {
            "prediction": float(prediction[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }
