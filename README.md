# CODSOFT_TASK3
# 🎵 Taylor Swift AI Song Recommendation System

## 📌 Project Overview

The Taylor Swift AI Song Recommendation System is a content-based recommendation system developed using Python and Streamlit.

The system recommends similar Taylor Swift songs based on song characteristics such as album, genre, mood, theme, and musical features.

It uses **TF-IDF Vectorization** and **Cosine Similarity**, two widely used Machine Learning techniques, to calculate the similarity between songs and generate personalized recommendations.

This project demonstrates the practical application of Artificial Intelligence in music recommendation systems.

---

## 🚀 Features

- 🎵 Recommend similar Taylor Swift songs
- 🤖 AI-based recommendation using TF-IDF
- 📊 Cosine Similarity algorithm
- 💖 Attractive Streamlit User Interface
- 🖼 Taylor Swift image integration
- 📀 Recommendation based on album, genre, mood, theme, and features
- ⚡ Fast and interactive interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pillow

---

## 🤖 AI Concepts Used

- Content-Based Recommendation System
- TF-IDF Vectorization
- Cosine Similarity
- Natural Language Processing (NLP)
- Feature Engineering

---

## 📂 Project Structure

```
Taylor_Swift_Recommendation/
│
├── app.py
├── songs.csv
├── taylor.jpg
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains approximately **100–150 popular Taylor Swift songs** collected from multiple albums.

Each song includes:

- Song Name
- Album
- Genre
- Mood
- Theme
- Features

These attributes are combined to generate AI-based recommendations.

---

## ▶ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User selects a Taylor Swift song.
2. The system combines song features into a single text representation.
3. TF-IDF converts text into numerical vectors.
4. Cosine Similarity measures similarity between songs.
5. The system recommends the top 5 most similar songs.

---

## 📥 Input

Select your favorite Taylor Swift song from the dropdown menu.

---

## 📤 Output

The application displays:

- Recommended Songs
- Album Name
- Genre
- Mood
- Similarity Score (%)

---

## 📈 Future Improvements

- Spotify API Integration
- YouTube Song Links
- Album-wise Filtering
- Mood-based Recommendation
- Favorite Songs Feature
- Artist Recommendation
- Audio Preview Support

---

## 👩‍💻 Author

**Dhruti**

AI Internship Project – CodSoft
