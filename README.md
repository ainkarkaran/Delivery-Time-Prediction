# Delivery-Time-Prediction

A Machine Learning web application that predicts the estimated food delivery time in minutes based on delivery-related factors such as distance, weather, traffic level, time of day, vehicle type, preparation time, and courier experience.

The project uses a Linear Regression model trained on a food delivery dataset and serves predictions through a FastAPI backend. A simple HTML, CSS, and JavaScript frontend is used to collect user input and display the predicted delivery time.

---

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Objective](#objective)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Features Used for Prediction](#features-used-for-prediction)
- [Model Training Workflow](#model-training-workflow)
- [Backend API Workflow](#backend-api-workflow)
- [Frontend Workflow](#frontend-workflow)
- [Installation](#installation)
- [How to Run the Project](#how-to-run-the-project)
- [API Documentation](#api-documentation)
- [Important Notes](#important-notes)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)

---

## Project Description

This project predicts food delivery time using a supervised machine learning approach.

The user enters delivery-related information through a web form. The frontend sends this data to the FastAPI backend. The backend loads the saved machine learning model and preprocessing pipeline, transforms the input data, predicts the delivery time, and returns the result to the frontend.

The final prediction is displayed in minutes.

---

## Dataset

Dataset used:

Food Delivery Time Prediction Dataset

Dataset link:

https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction

The dataset contains food delivery order records with features such as distance, weather, traffic level, time of day, vehicle type, preparation time, courier experience, and actual delivery time.

---

## Objective

The objective of this project is to build a simple end-to-end machine learning application that:

1. Trains a Linear Regression model on food delivery data.
2. Saves the trained model and preprocessing pipeline.
3. Uses FastAPI to expose the trained model as an API.
4. Uses a frontend form to collect input from the user.
5. Sends the input data from frontend to backend using JavaScript.
6. Displays the predicted delivery time in minutes.

---

## Technologies Used

### Machine Learning

- Python
- Pandas
- Scikit-learn
- Linear Regression
- OneHotEncoder
- ColumnTransformer
- Joblib

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript
- Fetch API

---

## Project Structure

```txt
Delivery-Time-Prediction/
│
├── server.py
├── app.html
├── style.css
├── script.js
├── model.pkl
├── preprocessor.pkl
├── train.py
├── dataset/
│   └── Food_Delivery_Dataset.csv
└── README.md
