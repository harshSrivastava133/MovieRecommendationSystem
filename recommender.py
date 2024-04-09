import pickle
pickle_in = open('cluster.pickle','rb')
pickle_df = open('my_dataframe.pkl','rb')
kmeans = pickle.load(pickle_in)#Loaded from file f
df = pickle.load(pickle_df)

labels = kmeans.labels_
centers = kmeans.cluster_centers_
df = df.drop(['id', 'release_year', 'runtime', 'genres',
       'production_countries', 'imdb_votes', 'tmdb_popularity',
       'tmdb_score', 'cast', 'director'],axis=1)
df['cluster_label'] = labels
def lower(text):
    return text.lower()

import numpy as np
import pandas as pd
def recommender(name):
    mov = (name.lower())
    filtered_df = df[df['title'].apply(lower) == mov]
    cluster_no = np.array(filtered_df['cluster_label'])
    combined_df = df[df['cluster_label'] == cluster_no[0]]
    for i in range(1,cluster_no.size):
        cluster = df[df['cluster_label'] == cluster_no[i]]
        combined_df = pd.concat([combined_df, cluster], ignore_index=True)
    top_movies = combined_df.sort_values(by='imdb_score', ascending=False).head(20)
    return top_movies

print("Enter The Name Of Movie Or TV Show:")
name = input()
print(recommender(name))

