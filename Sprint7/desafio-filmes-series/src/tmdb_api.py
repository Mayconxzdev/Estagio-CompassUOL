import os
from tmdbv3api import TMDb, Movie, TV

tmdb = TMDb()
tmdb.api_key = os.getenv('TMDB_API_KEY')  # Certifique-se de definir a variável de ambiente

def get_movie_details(movie_id):
    movie = Movie()
    return movie.details(movie_id)

def get_tv_show_details(tv_id):
    tv = TV()
    return tv.details(tv_id)

def search_movies(query):
    movie = Movie()
    return movie.search(query)

def search_tv_shows(query):
    tv = TV()
    return tv.search(query)

def get_popular_movies(page=1):
    movie = Movie()
    return movie.popular(page=page)

def get_popular_tv_shows(page=1):
    tv = TV()
    return tv.popular(page=page)