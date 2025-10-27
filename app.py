import os
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# ---------------------------------
# Setup
# ---------------------------------
load_dotenv()

app = Flask(__name__)

# ---------------------------------
# Load dataset
# ---------------------------------
print("Loading dataset...")
songs_df = pd.read_csv(os.path.join("data", "spotify_songs.csv"))


# Combine fields to create description text
songs_df["description"] = (
    songs_df["track_name"].astype(str)
    + " by "
    + songs_df["track_artist"].astype(str)
    + " — genre: "
    + songs_df["playlist_genre"].astype(str)
)

# ---------------------------------
# Load precomputed embeddings
# ---------------------------------
embeddings_path = os.path.join("instance", "song_embeddings.npy")

if not os.path.exists(embeddings_path):
    raise FileNotFoundError("Embeddings file not found in 'instance/song_embeddings.npy'!")

print("Loading precomputed embeddings...")
song_embeddings = np.load(embeddings_path)

# Load embedding model for user mood input
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------------------
# Helper function for cosine similarity
# ---------------------------------
def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# ---------------------------------
# Routes
# ---------------------------------
@app.route("/")
def index_route():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_input = request.form.get("prompt", "").strip()
    n_recs = int(request.form.get("n_recs", 5))  # default to 5 if not provided
    top_k = int(request.form.get("top_k", 10))   # optional: number of top candidates

    if not user_input:
        return render_template("results.html", prompt=user_input, recommendations=None)

    print(f"Generating recommendations for mood: {user_input} | Top_k={top_k}, Results={n_recs}")

    # Encode mood using the local model
    mood_embedding = model.encode([user_input])[0]

    # Compute similarities
    similarities = np.array([
        cosine_similarity(mood_embedding, song_emb)
        for song_emb in song_embeddings
    ])

    # Attach similarity scores and filter results
    songs_df["similarity"] = similarities
    recommendations = (
        songs_df.sort_values("similarity", ascending=False)
        .drop_duplicates(subset=["track_name", "track_artist"])
        .head(top_k)  # pick top candidates first
        .head(n_recs)  # then trim to number of results requested
    )

    # Format results for the template
    rec_list = [
        f"{row['track_name']} by {row['track_artist']} ({row['playlist_genre']})"
        for _, row in recommendations.iterrows()
    ]

    return render_template("results.html", prompt=user_input, recommendations=rec_list)


# ---------------------------------
# Run the Flask app
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)
