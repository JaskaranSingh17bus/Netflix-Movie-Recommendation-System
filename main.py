import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# E.D.A
print('\nMovies Data:\n')
print(movies.head())

print('\nRatings Data:\n')
print(ratings.head())


print('\nMovies Info:\n')
print(movies.info())

print('\nRatings Info:\n')
print(ratings.info())

print("\n\nShape of Movies Data:", movies.shape)
print("\n\nShape of Ratings Data:", ratings.shape)

# Description of Data
print("\n\nMovies Data Description:\n\n", movies.describe())
print("\n\nRatings Dat Description:\n\n", ratings.describe())

# Checking Missing Values
print("\n\nMissing Values in Movies Data:", movies.isnull().sum())
print("\n\nMissing Values in Ratings Data:", ratings.isnull().sum())

# Merging Data (doubt have to undersant)
df = pd.merge(movies, ratings, on='movieId')

ratings_summary = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings_summary['num of ratings'] = df.groupby('title')['rating'].count()

print("\n\nRating Summary :\n\n", ratings_summary.head())
print("\n\nRating Summary info:\n\n", ratings_summary.info())
print("\n\nRating Summary Description:\n\n", ratings_summary.describe())
print("\n\nRating Summary Shape:\n\n", ratings_summary.shape)

# Visualizing Data
plt.figure(figsize=(10, 6))
sns.histplot(ratings_summary['rating'], bins=70, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Number of Ratings')
plt.ylabel('Count of Moives')
plt.show()
plt.close()

top_10_movies  =  ratings_summary.sort_values('num of ratings', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_movies['num of ratings'], y=top_10_movies.index, palette='viridis')
plt.title('Top 10 Movies by Number of Ratings')
plt.xlabel('Number of Ratings') 
plt.ylabel('Movie Title')
plt.show()
plt.close()

# Recommender System
moviemat = df.pivot_table(index='userId', columns='title', values='rating')
print("\n\nMovie Matrix:\n\n", moviemat.head())

starwars_user_ratings = moviemat['Star Wars: Episode IV - A New Hope (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars = corr_starwars.join(ratings_summary['num of ratings'])

print(corr_starwars.sort_values('Correlation', ascending=False).head(10))

recommendations = corr_starwars[corr_starwars['num of ratings'] > 100].sort_values('Correlation', ascending=False)
print(recommendations.head(10))


liarliar_user_ratings = moviemat['Liar Liar (1997)']
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings_summary['num of ratings'])

# 100 se zyada ratings wali top 5 movies
print("\n--- Recommendations for Liar Liar ---")
print(corr_liarliar[corr_liarliar['num of ratings'] > 100].sort_values('Correlation', ascending=False).head(6))

def get_recommendations(movie_name):
    # User ratings lena
    user_ratings = moviemat[movie_name]
    
    # Correlation nikalna
    similar_movies = moviemat.corrwith(user_ratings)
    corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
    corr_df.dropna(inplace=True)
    corr_df = corr_df.join(ratings_summary['num of ratings'])
    
    # Return Top 5 recommendations
    return corr_df[corr_df['num of ratings'] > 100].sort_values('Correlation', ascending=False).head(6)

# Test karo function ko
print(get_recommendations('Toy Story (1995)'))

import pickle
pickle.dump(moviemat, open('moviemat.pkl', 'wb'))
pickle.dump(ratings_summary, open('ratings_summary.pkl', 'wb'))

