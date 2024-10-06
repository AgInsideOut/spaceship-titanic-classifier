import os
import sys
import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import joblib
import numpy as np

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

try:
    model_path = 'best_model.joblib'
    if not os.path.exists(model_path):
        logger.error(f"Model file not found: {model_path}")
        raise FileNotFoundError(f"Model file not found: {model_path}")

    best_model = joblib.load(model_path)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    logger.error(traceback.format_exc())
    sys.exit(1)


class InputData(BaseModel):
    CryoSleep: int
    Age: float
    VIP: int
    RoomService: float
    FoodCourt: float
    ShoppingMall: float
    Spa: float
    VRDeck: float
    Cabin_num: float
    HomePlanet_Earth: int
    HomePlanet_Europa: int
    HomePlanet_Mars: int
    HomePlanet_Unknown: int
    Destination_55_Cancri_e: int
    Destination_PSO_J318_5_22: int
    Destination_TRAPPIST_1e: int
    Destination_Unknown: int
    Deck_A: int
    Deck_B: int
    Deck_C: int
    Deck_D: int
    Deck_E: int
    Deck_F: int
    Deck_G: int
    Deck_T: int
    Deck_Unknown: int
    Side_P: int
    Side_S: int
    Side_Unknown: int
    Transported: Optional[int] = None


@app.post("/predict")
async def predict(data: InputData):
    try:
        input_data = np.array([[
            data.CryoSleep, data.Age, data.VIP,
            data.RoomService, data.FoodCourt, data.ShoppingMall, data.Spa,
            data.VRDeck, data.Cabin_num, data.HomePlanet_Earth, data.HomePlanet_Europa,
            data.HomePlanet_Mars, data.HomePlanet_Unknown, data.Destination_55_Cancri_e,
            data.Destination_PSO_J318_5_22, data.Destination_TRAPPIST_1e,
            data.Destination_Unknown, data.Deck_A, data.Deck_B, data.Deck_C, data.Deck_D,
            data.Deck_E, data.Deck_F, data.Deck_G, data.Deck_T, data.Deck_Unknown,
            data.Side_P, data.Side_S, data.Side_Unknown
        ]])

        prediction = best_model.predict(input_data)
        logger.info(f"Prediction made: {prediction[0]}")
        return {"prediction": int(prediction[0])}
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/")
async def root():
    return {"message": "Welcome to the Spaceship Titanic Classifier"}


@app.get("/transport")
async def transport_check():
    return {"status": "transported"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
