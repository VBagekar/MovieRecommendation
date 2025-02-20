# %%
import numpy as np

# %%
import pandas as pd


# %%
movies=pd.read_csv('./data/movies.csv')
credits=pd.read_csv('./data/credits.csv')
movies.head()

# %%
movies=movies.merge(credits,on='title')
movies.head()

# %%
# genres id keywords title overview cast crew
movies=movies[['movie_id','title','genres','keywords','overview','cast','crew']]
movies.head()

# %%
movies.isnull().sum()


# %%
movies.dropna(inplace=True)


# %%
movies.duplicated().sum()


# %%
movies.iloc[0].genres


# %%
import ast
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

# %%
movies['genres']=movies['genres'].apply(convert)


# %%
movies['keywords']=movies['keywords'].apply(convert)

# %%

def convert3(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter!=3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

# %%
movies['cast']=movies['cast'].apply(convert3)

# %%


def fetch_director(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

# %%
movies['crew']=movies['crew'].apply(fetch_director)

# %%
movies.head()

# %%
movies['overview']=movies['overview'].apply(lambda x:x.split())

# %%
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])    

# %%
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

# %%
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])

# %%
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])

# %%
movies.head()

# %%
movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew'] 

# %%
new_df=movies[['movie_id','title','tags']]

# %%
new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))

# %%
new_df.head()

# %%
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())

# %%



