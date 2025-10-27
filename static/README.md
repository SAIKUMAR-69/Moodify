# 🎧 Moodify – AI-Powered Song Recommender

Moodify is an intelligent music recommendation web app that suggests songs based on your **mood**, **vibe**, or **activity**. It uses **semantic search** powered by `SentenceTransformers` and a Spotify dataset to find the perfect tracks for every feeling.

---

## 🚀 Features

- 🎵 Mood-based song recommendations
- ⚡ Fast semantic search using locally precomputed embeddings
- 💾 Caches embeddings for instant results
- 🧠 Powered by `SentenceTransformers (all-MiniLM-L6-v2)`
- 🎨 Modern UI built with Flask + HTML/CSS
- 💚 Inspired by Spotify’s listening experience

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Moodify.git
cd Moodify
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
# OR
source venv/bin/activate  # (Mac/Linux)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare Data

Place your Spotify dataset inside the `data/` folder:
```
data/spotify_songs.csv
```

### 5️⃣ Run the App

```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
Moodify/
│
├── data/
│   └── spotify_songs.csv
│
├── instance/
│   └── song_embeddings.npy
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 💡 Tech Stack

- **Backend:** Flask (Python)
- **AI Model:** SentenceTransformers (all-MiniLM-L6-v2)
- **Frontend:** HTML, CSS
- **Data:** Spotify song dataset
- **Storage:** NumPy Embeddings Cache

---

## 🧩 Future Enhancements

- 🎤 Add voice-based mood input
- 💬 Integrate with OpenAI or OpenRouter API for emotion analysis
- 🔊 Direct Spotify API integration
- 🌈 Personalized playlists

---

## ⚙️ Git Setup

```bash
git init
git add .
git commit -m "Initial commit - Moodify project"
git branch -M main
git remote add origin https://github.com/yourusername/Moodify.git
git push -u origin main
```

✅ **Make sure to ignore sensitive files:**
```
.env
instance/
__pycache__/
```

---

## 🧠 Credits

Developed by **Saikumar**  
Powered by **Flask + SentenceTransformers + Spotify Dataset**
