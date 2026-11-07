from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_FILE = Path(__file__).resolve().parent / "movies.csv"

def recommend(preference, count=5):
    data = pd.read_csv(DATA_FILE).fillna("")
    if data.empty:
        return []
    content = data["title"] + " " + data["genre"] + " " + data["description"]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(content)
    query = vectorizer.transform([preference])
    scores = cosine_similarity(query, matrix).ravel()
    order = scores.argsort()[::-1]
    results = []
    for idx in order:
        if scores[idx] <= 0:
            continue
        results.append({
            "title": data.iloc[idx]["title"],
            "genre": data.iloc[idx]["genre"],
            "score": float(scores[idx])
        })
        if len(results) >= count:
            break
    return results
