from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import joblib
from xgboost import XGBRegressor

app = FastAPI(title="Happiness Score Prediction API")

# Load model dan scaler
with open("XGBoost_Model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["scaler"]

# Input schema disesuaikan dengan 7 fitur
class HappinessData(BaseModel):
    GDP_per_capita: float
    Social_support: float
    Healthy_life_expectancy: float
    Freedom_to_make_life_choices: float
    Generosity: float
    Perceptions_of_corruption: float
    GDP_per_Score: float

# Output schema
class PredictionResponse(BaseModel):
    predicted_score: float

@app.get("/")
def read_root():
    return {"message": "✅ Happiness Score Prediction API is running!"}

# Preprocessing input
def preprocess_input(data: HappinessData):
    df = pd.DataFrame([data.dict()])
    df.columns = [
        'GDP per capita', 'Social support', 'Healthy life expectancy',
        'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',
        'GDP per Score'
    ]
    df_scaled = scaler.transform(df)
    return pd.DataFrame(df_scaled, columns=df.columns)

@app.post("/predict", response_model=PredictionResponse)
def predict_score(data: HappinessData):
    processed = preprocess_input(data)
    prediction = model.predict(processed)[0]
    return {"predicted_score": round(float(prediction), 3)}
