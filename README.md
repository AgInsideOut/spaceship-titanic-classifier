# Spaceship Titanic Classifier

This repository contains the deployment code for the Spaceship Titanic Passenger Transport prediction model, specifically designed to predict whether a passenger was transported to an alternate dimension during the Spaceship Titanic's collision with the spacetime anomaly.

## Table of Contents

- [Project Structure](#project-structure)
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)
- [Model Information](#model-information)
- [Authors](#authors)
- [License](#license)
- [Dataset License](#dataset-license)
- [Acknowledgments](#acknowledgments)

## Project Structure

```plaintext
spaceship-titanic-classifier/
│
├── README.md
├── LICENSE
├── requirements.txt
├── Dockerfile
├── entrypoints.sh
├── .gitignore
├── main.py
├── best_model.joblib
└── test/
    └── test_api.py
```

This structure outlines the main components of the project.

## Introduction

The Spaceship Titanic Classifier API is a machine learning-based service that predicts whether a passenger was transported to an alternate dimension during the Spaceship Titanic's collision with the spacetime anomaly. This API leverages a trained model to provide real-time predictions based on various passenger features.

### Dataset

This project utilizes the [Spaceship Titanic Dataset](https://www.kaggle.com/competitions/spaceship-titanic/overview) from Kaggle, which contains personal records of passengers.

## Installation

These instructions will help you set up the project on your local machine.

1. Clone the repository:

    ```bash
    git clone https://github.com/AgInsideOut/spaceship-titanic-classifier.git
    ```

2. Navigate to the project directory:

    ```bash
    cd spaceship-titanic-classifier
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The API is live and can be accessed at:
<https://spaceship-titanic-classifier.onrender.com>

To run the API locally:

1. Ensure you're in the project directory.
2. Run the following command:

    ```bash
    uvicorn main:app --reload
    ```

3. The API will be available at `http://localhost:8000`.

## API Endpoints

Base URL: <https://spaceship-titanic-classifier.onrender.com>

1. **Root Endpoint**
   - **URL**: `https://spaceship-titanic-classifier.onrender.com/`
   - **Method**: GET
   - **Description**: Welcome message for the API.
   - **Response**: `{"message": "Welcome to the Stroke Prediction API"}`

2. **Prediction Endpoint**
   - **URL**: `https://spaceship-titanic-classifier.onrender.com/predict`
   - **Method**: POST
   - **Description**: Predicts whether a passenger was transported to an alternate dimension based on input features.
   - **Request Body**: JSON object with the following fields:

     ```json
     {
      "CryoSleep": int,
      "Age": float,
      "VIP": int,
      "RoomService": float,
      "FoodCourt": float,
      "ShoppingMall": float,
      "Spa": float,
      "VRDeck": float,
      "Cabin_num": int,
      "HomePlanet_Earth": int,
      "HomePlanet_Europa": int,
      "HomePlanet_Mars": int,
      "HomePlanet_Unknown": int,
      "Destination_55_Cancri_e": int,
      "Destination_PSO_J318_5_22": int,
      "Destination_TRAPPIST_1e": int,
      "Destination_Unknown": int,
      "Deck_A": int,
      "Deck_B": int,
      "Deck_C": int,
      "Deck_D": int,
      "Deck_E": int,
      "Deck_F": int,
      "Deck_G": int,
      "Deck_T": int,
      "Deck_Unknown": int,
      "Side_P": int,
      "Side_S": int,
      "Side_Unknown": int
     }
     ```

   - **Response**: `{"prediction": int}` (0 for not transported, 1 for transported)

## Testing the API

You can test the live API using curl or any API testing tool. Here's an example using curl:

```bash
curl -X POST "https://spaceship-titanic-classifier.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -d '{
        "CryoSleep": 0,
        "Age": 65.0,
        "VIP": 1,
        "RoomService": 0.0,
        "FoodCourt": 0.0,
        "ShoppingMall": 0.0,
        "Spa": 0.0,
        "VRDeck": 0.0,
        "Cabin_num": 0,
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
     }'
```

## Model Information

The model used in this API is an Stacking Ensemble (XGB + CatBoost) trained to predict whether the passenger was transported or not. Here are some key performance metrics:

- **Accuracy**: 0.8028 (+/- 0.0095)
- **Precision**: 0.7881 (+/- 0.0140)
- **Recall**: 0.8324 (+/- 0.0163)
- **F1 Score**: 0.8096 (+/- 0.0089)
- **F-beta Score**: 0.8096 (+/- 0.0089)
- **ROC AUC**: 0.8026 (+/- 0.0095)
- **Balanced Accuracy**: 0.8026 (+/- 0.0095)

### Key Points

1. The model is particularly effective in identifying transported passengers.
2. It balances precision and recall, making it suitable for applications where both metrics are important.
3. The model's performance metrics indicate a reliable predictive capability.

## Authors

- **Agnieszka Thiel** - *Initial work* - [AgInsideOut](https://github.com/AgInsideOut)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/AgInsideOut/spaceship-titanic-classifier/blob/main/LICENSE) file for details.

## Dataset License

The Stroke Prediction Dataset is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Acknowledgments

- Inspiration and Data Source - [Spaceship Titanic Competition](https://www.kaggle.com/c/spaceship-titanic)
- Project Requirements: [Turing College](https://github.com/TuringCollegeSubmissions)
