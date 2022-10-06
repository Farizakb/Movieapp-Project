from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CommentForm
from .models import Comment, Movie, Slider




def index(request):
    movies = Movie.objects.filter(is_active = True,is_home=True)
    sliders = Slider.objects.filter(is_active=True)
    return render(request, "movies/index.html",{
       "movies":movies,
       "sliders":sliders
    })

def movies(request):
    movies = Movie.objects.filter(is_active = True,is_home=True)

    return render(request,"movies/movies.html",{
        "movies":movies
    })
    

def movie_detail(request,slug):
    
    movies = Movie.objects.all()
    currentMovie = [movie    for movie in movies if movie.slug == slug][0]
    print("kecdi")
    if request.method == "POST":
        print("kecdi")
        form = CommentForm(request.POST)
        
        if form.is_valid():
            print("kecdi")
            comment = form.save(commit=False)
            comment.film = currentMovie
            comment.save()
            return HttpResponseRedirect(reverse("movie-det",args=[slug]))
        else:
            return  render(request, "movies/movies_details.html",{
            "movie":currentMovie,
            "genres":currentMovie.genre.all(),
            "people":currentMovie.people.all(),
            "videos":currentMovie.video.all(),
            "comments":currentMovie.comments.all().order_by('-creating_at'),
            "form":form,
        })
            
    form = CommentForm()
    
    return  render(request, "movies/movies_details.html",{
        "movie":currentMovie,
        "genres":currentMovie.genre.all(),
        "people":currentMovie.people.all(),
        "videos":currentMovie.video.all(),
        "comments":currentMovie.comments.all().order_by('-creating_at'),
        "form":form,
    })
    
     