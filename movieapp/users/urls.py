from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_req, name="login"),
    path("register", views.register_req, name="register"),
    path("logout", views.logout_req, name="logout"),
    path("change-password", views.change_password, name="change_password"),
    path("profile", views.profile, name="profile"),
    path("watch-list", views.watch_list, name="watch_list"),
]
