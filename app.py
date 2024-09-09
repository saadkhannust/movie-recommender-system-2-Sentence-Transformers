# app.py
import streamlit as st
import requests
import pandas as pd

st.title('Movie Recommender System')

# Load the data
new_df = pd.read_csv('/kaggle/working/cleaned_tmdb_movies.csv')
movie_list = new_df['title'].values

movie_name = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    if movie_name:
        response = requests.post("http://localhost:8000/recommend/", json={"movie_name": movie_name})
        recommendations = response.json().get("recommendations", [])
        
        if recommendations:
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommendations[0])
            with col2:
                st.text(recommendations[1])
            with col3:
                st.text(recommendations[2])
            with col4:
                st.text(recommendations[3])
            with col5:
                st.text(recommendations[4])
        else:
            st.write("No recommendations found.")
    else:
        st.write("Please select a movie.")
