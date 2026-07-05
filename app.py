import streamlit as st
import pandas as pd
from PIL import Image
#python -m streamlit run app.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


songs = pd.read_csv("songs.csv")
print(songs.head())


songs = songs.fillna("")

# Create Combined Features
songs["combined_features"] = (
    songs["album"] + " " +
    songs["genre"] + " " +
    songs["mood"] + " " +
    songs["theme"] + " " +
    songs["features"]
)

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(songs["combined_features"])

# Cosine Similarity
similarity = cosine_similarity(tfidf_matrix)

# Song Index
indices = pd.Series(
    songs.index,
    index=songs["song"]
).drop_duplicates()



st.set_page_config(
    page_title="Taylor Swift AI Recommendation",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<h1 style="
text-align:center;
color:#FF69B4;
font-size:48px;
font-weight:bold;
margin-top:-10px;
margin-bottom:10px;
font-family:Georgia;
">
🎵 Taylor Swift AI Song Recommendation
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style="
text-align:center;
color:#DB7093;
margin-top:-10px;
">
✨ Discover Songs with Artificial Intelligence ✨
</h3>
""", unsafe_allow_html=True)


image = Image.open("taylor.jpg")


# ================= HERO SECTION =================

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2,1,2])

with c2:
    st.image(image, width=280)



st.markdown("""
<div style="
background:#FFF0F5;
padding:20px;
border-radius:18px;
border:2px solid #FFC0CB;
">

<h2 style="
text-align:center;
color:#FF69B4;
font-family:Georgia;
">
🩷 Hey, Swiftie!
</h2>

<div style="
text-align:center;
font-size:16px;
color:#FF69B4;
line-height:1.8;
font-family:Georgia;
">

✨ Every Taylor Swift song tells a story.

<br><br>

Let AI discover songs with the same vibe using
<b>TF-IDF</b> & <b>Cosine Similarity</b>.

<br><br>

🎵 Pick your favorite track and enjoy your personalized recommendations! 💖

</div>

</div>
""", unsafe_allow_html=True)
#st.markdown("<br>", unsafe_allow_html=True)



st.markdown("""
<h3 style="color:#FF69B4;">
🎶 Choose Your Favorite Song
</h3>
""", unsafe_allow_html=True)

selected_song = st.selectbox(
    "",
    songs["song"].sort_values()
)



def recommend_songs(song_name, top_n=5):

    if song_name not in indices:
        return None

    idx = indices[song_name]

    similarity_scores = list(enumerate(similarity[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:top_n+1]

    recommended = []

    for i, score in similarity_scores:
        recommended.append({
            "Song": songs.iloc[i]["song"],
            "Album": songs.iloc[i]["album"],
            "Genre": songs.iloc[i]["genre"],
            "Mood": songs.iloc[i]["mood"],
            "Similarity": round(score * 100, 2)
        })

    return pd.DataFrame(recommended)









if st.button("✨ Recommend Songs"):

    recommendations = recommend_songs(selected_song)

    if recommendations is not None:

        st.success("💖 AI Recommended Songs")

        st.dataframe(
            recommendations,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.error("Song Not Found")