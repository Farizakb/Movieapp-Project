from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator,MaxValueValidator
from ckeditor.fields import RichTextField
# Create your models here.

    
     
    

class Genre(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    mail = models.EmailField(max_length=150)
    number = models.IntegerField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.mail


class Person(models.Model):
    
    cins = (
        ("K","Male"),
        ("Q","Female")
    )
    statu = (
        ("1","Xidmeti"),
        ("2","Oyuncu"),
        ("3","Yonetmen"),
        ("4","Yazar"),
    )
    
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    biograpy = models.CharField(max_length=3000)
    img = models.FileField(upload_to="images")
    birth = models.DateField()
    gender = models.CharField(max_length=1,choices=cins)
    duty = models.CharField(max_length=1,choices=statu)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE,null=True,blank=True,related_name="person")
    
    @property
    def full_name(self):
        return f"{self.name} {self.surname} "
    
    def __str__(self):
        return f"{self.name} {self.surname} ({self.statu[int(self.duty)-1][1]})"
    


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    img = models.FileField(upload_to = "images")
    img_cover = models.FileField(upload_to = "images")
    duration = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    budget = models.DecimalField(max_digits=19,decimal_places=2, null=True)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    lang = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre,related_name="movie")
    people = models.ManyToManyField(Person,related_name="movie")
    slug = models.SlugField(default="",blank=True,null=False,unique=True, db_index=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    review = models.TextField(blank=True, null=True)
    creating_at = models.DateTimeField(null = True, auto_now=True)
    film = models.ForeignKey(Movie, related_name="comments",on_delete=models.CASCADE)
    stars = models.IntegerField(null = True)
    

class Video(models.Model):
    title = models.CharField(max_length=200) 
    link = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie,related_name="video",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
    
class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "images")
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL,null = True , blank = True)
    is_active = models.BooleanField(default=False)
    