# MoodLens-API
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

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
│── sent_app.py # FastAPI app code <br>
│── requirements.txt # Python dependencies <br>
│── .gitignore # Ignore ML models, env files, etc. <br>
│── README.md # Project description <br>
│── start.sh # Optional: script to start the API <br>

> **Note:** ML model files (`.joblib`) are **not included** in the repo to keep it lightweight.  
> Download models separately or store them in cloud storage for production.

---

## Installation

1. Clone the repository:
`bash` <br>
`git clone https://github.com/nyarderr/moodlens-api.git` <br>
`cd moodlens-api` <br>

2. Install dependencies
`pip install -r requirements.txt` <br>

3. Place your trained model files (model.joblib, vectorizer.joblib, label_encoder.joblib) in the project root. <br>

---

## Running the API

### Locally <br>
   `bash ` <br>
   `uvicorn sent_app:app --reload` <br>
   Visit http://127.0.0.1:8000/docs for interactive API docs (Swagger UI). <br>


### API EndPoints

1. Health Check <br>
   `bash` <br>
   `GET /health` <br>
   Response; <br>
   `json` <br>
   `{"status":"ok,"model":"loaded"}` <br>


2. Predict Sentiment <br>
   `bash` <br>
   `POST /predict` <br>
   PayLoad; <br>
   `json` <br>
   `{"text":"I love this product"}`- single text OR <br>
   `{"text": ["I love this!", "This is terrible."]}` - batch input (list of texts) <br>
   Response; <br>
   `json` <br>
   `{"Sentiment":"positive","Confidence:0.92}` OR <br>
   `[{"text": "I love this!", "Sentiment":"positive", "Confidence":0.93},{"text": "This is terrible.", "Sentiment":"negative", "Confidence":0.83}]` <br>

---

## Deployment

- Recommended platforms: Render, Heroku, AWS, GCP

- Use uvicorn sent_app:app --host 0.0.0.0 --port $PORT as the start command.

- Ensure model files are accessible in production (local or cloud storage).
   
   















