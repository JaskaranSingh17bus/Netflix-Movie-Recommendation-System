import streamlit as st
import pickle
import pandas as pd

# Page Title
st.title('Netflix Movie Recommender')

# Data load karo jo humne save kiya tha
moviemat = pickle.load(open('moviemat.pkl', 'rb'))
ratings_summary = pickle.load(open('ratings_summary.pkl', 'rb'))

# Movie selection dropdown
movie_list = moviemat.columns.values
selected_movie = st.selectbox("which movies you like?", movie_list)

if st.button('Recommend Karo'):
    # Wahi logic jo tune pehle likha tha
    user_ratings = moviemat[selected_movie]
    similar_movies = moviemat.corrwith(user_ratings)
    
    corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
    corr_df.dropna(inplace=True)
    corr_df = corr_df.join(ratings_summary['num of ratings'])
    
    # Top 5 Recommendations
    recommendations = corr_df[corr_df['num of ratings'] > 100].sort_values('Correlation', ascending=False).iloc[1:6]
    
    st.write("Ye rahi tere liye top 5 movies:")
    for movie in recommendations.index:
        st.success(movie)