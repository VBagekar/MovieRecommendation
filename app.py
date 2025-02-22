import streamlit as st
import pickle
import pandas as pd

# Load the movie data
movies_df = pickle.load(open('movies.pkl', 'rb'))  # Keep it as a DataFrame
movies_list = movies_df['title'].values  # Extract movie titles as an array

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    
    movie_idx = movies_df[movies_df['title'] == movie].index[0]
    
    # Get index of the selected movie
    try:
        movie_index = movies_df[movies_df['title'] == movie].index[0]
    except IndexError:
        return ["Movie not found in database"]
    
    # Get similarity scores
    distances = similarity[movie_index]
    
    # Get top 5 similar movies (excluding the selected one)
    movie_indices = sorted(
        list(enumerate(distances)), 
        reverse=True, key=lambda x: x[1]
    )[1:6]
    
    # Retrieve movie titles
    recommended_movies = [movies_df.iloc[i[0]].title for i in movie_indices]
    
    return recommended_movies

# Streamlit UI
st.title("🎬 Movie Recommender System")

# Movie selection dropdown
selected_movie_name = st.selectbox('🎥 Select a movie:', movies_list)

# Recommendation button
if st.button('🎞️ Recommend'):
    st.subheader(f"Movies similar to **{selected_movie_name}**:")
    
    # Fetch recommendations
    recommendations = recommend(selected_movie_name)
    
    # Display recommendations
    for movie in recommendations:
        st.write(f"🎬 {movie}")
