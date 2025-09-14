from fastapi import FastAPI
import joblib
from pydantic import BaseModel
from typing import Union


model = None
vectorizer = None
le = None

app = FastAPI(title="MoodLens-API")

model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")
le = joblib.load("label_encoder.joblib")


@app.get('/')
def root():
    return RedirectResponse(url="/docs")


@app.get('/health')
def health():
    return {"status":"ok",
            "model":"loaded" if model is not None else "not loaded",
           "vectorizer":"loaded" if vectorizer is not None else "not loaded",
           "label_encoder":"loaded" if le is not None else "not loaded"}


class TextInput(BaseModel): 
    text: Union[str, list[str]]

@app.post('/predict')
def predict_sentiment(data: TextInput):
    
    text = data.text
    
    #------- Single text input ----------
    if isinstance(text, str):
        X = vectorizer.transform([text])

        pred = model.predict(X)[0] # [0] extracts int
        pred_label = le.inverse_transform([pred])[0]  # []; expects array, 0 extracts neg
        probs = model.predict_proba(X)[0]  # [0] takes array out of list
        prob = probs[pred]   # selects prob based on pred.

        return {
            "Sentiment":pred_label,
            "Confidence":float(prob)
        }

    #------ batch input --------------
    elif all(isinstance(item, str) for item in text):
        
        X = vectorizer.transform(text)

        pred = model.predict(X)
        pred_label = le.inverse_transform(pred)
        prob = model.predict_proba(X).max(axis=1)

        results = []
        for txt,pr_label, probab in zip(text,pred_label, prob):
            results.append({
                "Text":txt,
                "Sentiment":pr_label,
                "Confidence":probab
            })

        return {"results":results}

    else:
        return {"error":"Input must be a string or list of strings"}
