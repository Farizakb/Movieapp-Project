from django.contrib import admin
from .models import Genre, Video, Contact, Movie, Person,Comment,Slider
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','is_active','is_home',)
    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('genre', 'lang','is_active','is_home',)
    search_fields = ('title','description',)
    list_editable = ('is_active','is_home')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','duty',)
    list_filter = ('gender','duty',)
    search_fields = ('name','surname','duty',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name','review','email','creating_at','film','stars')
    search_fields = ('review', 'film__title')
    
    
    
admin.site.register(Genre)
admin.site.register(Slider)
admin.site.register(Video)
admin.site.register(Contact)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Comment,CommentAdmin)