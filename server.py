from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib
import os


app = FastAPI(title="Food Delivery Time Prediction API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")


class DeliveryInput(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: float
    Courier_Experience_yrs: float


@app.get("/")
def open_app():
    return FileResponse("app.html")


@app.get("/style.css")
def get_css():
    return FileResponse("style.css")


@app.get("/script.js")
def get_js():
    return FileResponse("script.js")


@app.post("/predict")
def predict_delivery_time(data: DeliveryInput):
    try:
        new_data = pd.DataFrame([{
            "Distance_km": data.Distance_km,
            "Weather": data.Weather,
            "Traffic_Level": data.Traffic_Level,
            "Time_of_Day": data.Time_of_Day,
            "Vehicle_Type": data.Vehicle_Type,
            "Preparation_Time_min": data.Preparation_Time_min,
            "Courier_Experience_yrs": data.Courier_Experience_yrs
        }])

        processed = preprocessor.transform(new_data)
        prediction = model.predict(processed)

        return {
            "success": True,
            "prediction": round(float(prediction[0]), 2),
            "unit": "minutes"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
