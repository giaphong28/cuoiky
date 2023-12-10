import streamlit as st
import pickle
import numpy as np
import requests
import streamlit.components.v1 as components
from streamlit_elements import elements, mui, html, sync
from streamlit_star_rating import st_star_rating
import pandas as pd

movies = pickle.load(open("movie_list.pkl", 'rb'))
similarity = np.load("similarity.npy")
movies_list=movies['title'].values
#import top 15 popular movies
top15 = pd.read_csv('top15_popular.csv',delimiter=',')

def fetch_topmovies():
    title = []
    id = []
    for i in top15['title']:
        title.append(i)
    for i in top15['id']:
        id.append(fetch_poster(i))  
    return title,id

def fetch_poster(movie_id):
  url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
  data=requests.get(url)
  data= data.json()
  poster_path = data['poster_path']
  full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
  return full_path

# st.header("Recent hot movies")
# imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")



# imageUrls = [
#     fetch_poster(1632),
#     fetch_poster(299536),
#     fetch_poster(17455),
#     fetch_poster(2830),
#     fetch_poster(429422),
#     fetch_poster(9722),
#     fetch_poster(13972),
#     fetch_poster(240),
#     fetch_poster(155),
#     fetch_poster(598),
#     fetch_poster(914),
#     fetch_poster(255709),
#     fetch_poster(572154)
   
#     ]


# imageCarouselComponent(imageUrls=imageUrls, height=200)


  
def recommend(movie):
    index=movies[movies['title']== movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster = []
    
    recommend_genre = []
    recommend_overview = []
    recommend_vote = []
    recommend_date = []
    
    for i in distance[0:9]:
      movies_id = movies.iloc[i[0]].id
      recommend_movie.append(movies.iloc[i[0]].title)
      recommend_genre.append(movies.iloc[i[0]].genre)
      recommend_overview.append(movies.iloc[i[0]].overview)
      recommend_vote.append(movies.iloc[i[0]].vote_average)
      recommend_date.append(movies.iloc[i[0]].release_date)
      recommend_poster.append(fetch_poster(movies_id))  
    return recommend_movie,recommend_poster,recommend_overview,recommend_genre,recommend_vote,recommend_date
# board, sidebar = st.columns((6,2))
# with board:
    # Initialize session state
st.session_state.text = st.session_state.get('text', 'selectvalue')

selectvalue=st.selectbox("Search or select movies from this dropdown", movies_list)

st.session_state['text']=selectvalue
movie_name,movie_poster,movies_overview,movie_genre,movie_vote,movie_date = recommend(st.session_state['text'])
movie_1,movie_2 = st.columns(2)
with movie_1:
    with elements(f'image'):
        html.img(src=movie_poster[0], css={"display": "block","margin-left": "auto","margin-right": "auto", "width":"50%",})
with movie_2:
    st.header(movie_name[0])
    st_star_rating("",maxValue=10,defaultValue=movie_vote[0],key="rating",read_only=True,size=20)
    st.write("""\n\n\n\n\n\n\n
                """)
    st.write("Thể loại: " + movie_genre[0])
    st.write("Tóm tắt: " + movies_overview[0])
    st.write("Ngày ra mắt: " + movie_date[0])        
    st.write("Đánh giá trung bình: " + movie_vote[0].astype("str"))


st.markdown("***")

if st.button("Show Recommend"):
    movie_name,movie_poster,movies_overview,movie_genre,movie_vote,movie_date = recommend(st.session_state['text'])
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col2:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col3:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col4:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    with col1:
        st.text(movie_name[5])
        st.image(movie_poster[5])
    with col2:
        st.text(movie_name[6])
        st.image(movie_poster[6])
    with col3:
        st.text(movie_name[7])
        st.image(movie_poster[7])
    with col4:
        st.text(movie_name[8])
        st.image(movie_poster[8])
# with sidebar:
#     st.write("sidebar")
#     top_title,top_id = fetch_topmovies()
#     i = 0
#     col1,col2,col3 = st.columns([1,2,2])
#     with elements(f'top'):
#         while(i<15):        
#             col1.write(i+1,unsafe_allow_html=True,)                       
#             col2.image(top_id[i],width=20)                
#             col3.write(top_title[i])
#             i = i + 1

