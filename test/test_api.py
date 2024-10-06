import requests

url = "https://spaceship-titanic-classifier.onrender.com/predict"
data = {
    "CryoSleep": 0,
    "Age": 65.0,
    "VIP": 1,
    "RoomService": 0.0,
    "FoodCourt": 0.0,
    "ShoppingMall": 0.0,
    "Spa": 0.0,
    "VRDeck": 0.0,
    "Cabin_num": 0.0,
    "HomePlanet_Earth": 0,
    "HomePlanet_Europa": 1,
    "HomePlanet_Mars": 0,
    "HomePlanet_Unknown": 0,
    "Destination_55_Cancri_e": 1,
    "Destination_PSO_J318_5_22": 0,
    "Destination_TRAPPIST_1e": 0,
    "Destination_Unknown": 0,
    "Deck_A": 0,
    "Deck_B": 0,
    "Deck_C": 0,
    "Deck_D": 0,
    "Deck_E": 0,
    "Deck_F": 0,
    "Deck_G": 0,
    "Deck_T": 1,
    "Deck_Unknown": 0,
    "Side_P": 1,
    "Side_S": 0,
    "Side_Unknown": 0
}

response = requests.post(url, json=data)
print(response.json())
