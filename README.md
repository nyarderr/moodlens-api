# MoodLens-API

**MoodLens-API** is a FastAPI-based REST API for sentiment analysis of text.  
It uses a trained scikit-learn model to classify text as **positive** or **negative**. <br>
The API supports both single and batch text predictions and is designed to integrate easily into chatbots, web apps, or other NLP pipelines.

---

## Features

- Predict sentiment for a single text input
- Predict sentiment for a batch of texts
- Returns predicted sentiment and confidence score
- Built with FastAPI for high performance and scalability
- Easy to deploy on platforms like Render, Heroku, or AWS

---

## Project Structure

moodlens-api/
│── sent_app.py # FastAPI app code
│── requirements.txt # Python dependencies
│── .gitignore # Ignore ML models, env files, etc.
│── README.md # Project description
│── start.sh # Optional: script to start the API

> **Note:** ML model files (`.joblib`) are **not included** in the repo to keep it lightweight.  
> Download models separately or store them in cloud storage for production.

---

## Installation

1. Clone the repository:
`bash`
`git clone https://github.com/nyarderr/moodlens-api.git`
`cd moodlens-api`

2. Install dependencies
`pip install -r requirements.txt`

3. Place your trained model files (model.joblib, vectorizer.joblib, label_encoder.joblib) in the project root.

---

## Running the API

Locally
   `bash `
   `uvicorn sent_app:app --reload`
   Visit http://127.0.0.1:8000/docs for interactive API docs (Swagger UI).


API EndPoints

1. Health Check
   `bash`
   `GET /health`
   Response;
   `json `
   `{"status":"ok,"model":"loaded"}`


2. Predict Sentiment
   `bash`
   `POST /predict`
   PayLoad;
   `json`
   `{"text":"I love this product"}`- single text OR
   `{"text": ["I love this!", "This is terrible."]}` - batch input (list of texts)
   Response;
   `json`
   `{"Sentiment":"positive","Confidence:0.92}` OR
   `[{"text": "I love this!", "Sentiment":"positive", "Confidence":0.93},{"text": "This is terrible.", "Sentiment":"negative", "Confidence":0.83}]`

---

## Deployment

- Recommended platforms: Render, Heroku, AWS, GCP

- Use uvicorn sent_app:app --host 0.0.0.0 --port $PORT as the start command.

- Ensure model files are accessible in production (local or cloud storage).
   
   













