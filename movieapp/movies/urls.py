from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name="home"),
    path("movies", views.movies, name="movies"),
    path("movies/<slug:slug>", views.movie_detail, name="movie-det"),   
    
]
