# Insurance Premium Predictor

A Machine Learning + FastAPI project that predicts an insurance premium category based on user information.

This project was built to strengthen my understanding of:
- Machine Learning pipelines using Scikit-learn
- FastAPI for serving ML models
- Pydantic for request validation
- Deploying a trained ML model as a REST API

## Features

- Predicts insurance premium category (Low, Medium, High)
- Input validation using Pydantic
- Automatic feature engineering using computed fields
- Scikit-learn Pipeline with ColumnTransformer and OneHotEncoder
- Interactive API documentation using Swagger UI

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Pydantic

## Machine Learning Workflow

- Data preprocessing using ColumnTransformer
- One-Hot Encoding for categorical features
- Random Forest Classifier
- Model serialization using Pickle
- REST API built with FastAPI

## Project Structure

```
.
├── premium_insurance_app.py
├── insurance_model.pkl
├── premium_insurance_prediction.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## Running the Project

1. Install the dependencies

```bash
pip install -r requirements.txt
```

2. Start the FastAPI server

```bash
uvicorn premium_insurance_app:app --reload
```

3. Open the API documentation

```
http://127.0.0.1:8000/docs
```

## Future Improvements

- Improve feature engineering
- Experiment with additional ML algorithms
- Build a frontend for easier interaction
- Deploy the application online
- Improve model accuracy with additional data and tuning

## Learning Outcome

This project was built as a hands-on exercise to revise core Machine Learning concepts while learning how to integrate a trained model with FastAPI. It helped me understand how to move from model training in a notebook to serving predictions through a production-style API.