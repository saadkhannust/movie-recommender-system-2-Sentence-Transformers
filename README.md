
# Movie Recommender System

### Description

This project is a Movie Recommender System built using the TMDB (The Movie Database) 5000 dataset. The system recommends movies similar to a given movie by analyzing metadata such as movie ID, name, overview, genre, cast, keywords, and crew. By creating tags from genre, cast, keywords, and crew information, the project utilizes sentence transformers for vectorization and calculates cosine similarity to find and recommend the top 5 movies similar to the selected movie. The project is deployed as an interactive web application using Streamlit.

### Folder Structure

movie-recommender-system.ipynb: Jupyter Notebook containing the code for creating the movie recommender system. Includes data preprocessing, vectorization, and similarity calculation.

tmdb_5000_credits.csv: Dataset containing movie credits (e.g., cast and crew information) used in the recommender system.

tmdb_5000_movies.csv: Dataset containing detailed movie metadata (e.g., movie names, overviews, genres) used in the recommender system.

app.py: Streamlit application script that serves the movie recommender system as a web app.

## Getting Started

### Clone the Repository
To get a copy of the project, clone the repository using:

git clone https://github.com/saadkhannust/movie-recommender-system-2-Sentence-Transformers.git

### Running the Code

Run the Kaggle Notebook

Import movie-recommender-system.ipynb.

Import bot the csv files: tmdb_5000_movies.csv and tmdb_5000_credits.csv

Explore the data processing, model creation, and UI creation steps.

Run the Streamlit Application

To run the Streamlit application, use the following commands:


!curl https://loca.lt/mytunnelpassword

!streamlit run app.py & npx localtunnel --port 8501 --subdomain=myuniquesubdomain

(Note: Replace myuniquesubdomain with your desired subdomain.)

The app will start in your browser, allowing you to input a movie and receive recommendations.

Contributors

Muhammad Saad Khan
