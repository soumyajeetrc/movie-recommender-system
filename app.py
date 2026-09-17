import streamlit as st
import pickle
import pandas as pd
import requests


# Fetch movie poster from TMDB
def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": st.secrets["TMDB_API_KEY"],
        "language": "en-US"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=(10, 30)
        )

        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

        return None

    except requests.exceptions.Timeout:
        st.error("TMDB connection timed out. Please check your internet connection and try again.")
        return None

    except requests.exceptions.RequestException as e:
        print("TMDB Error:", e)
        return None


# Recommend movies
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        # Fetch poster from TMDB
        poster = fetch_poster(movie_id)

        recommended_movies_posters.append(poster)

    return recommended_movies, recommended_movies_posters


# Load movie data
movies_dict = pickle.load(
    open('movie_dict.pkl', 'rb')
)

movies = pd.DataFrame(movies_dict)


# Load similarity matrix
similarity = pickle.load(
    open('similarity.pkl', 'rb')
)


# Streamlit application
st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)


# Recommend button
if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])

        if posters[0]:
            st.image(posters[0])
        else:
            st.write("Poster unavailable")


    with col2:
        st.text(names[1])

        if posters[1]:
            st.image(posters[1])
        else:
            st.write("Poster unavailable")


    with col3:
        st.text(names[2])

        if posters[2]:
            st.image(posters[2])
        else:
            st.write("Poster unavailable")


    with col4:
        st.text(names[3])

        if posters[3]:
            st.image(posters[3])
        else:
            st.write("Poster unavailable")


    with col5:
        st.text(names[4])

        if posters[4]:
            st.image(posters[4])
        else:
            st.write("Poster unavailable")