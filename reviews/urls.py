from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.detail, name="detail"),
    path("movie_register/", views.movie_register, name="movie_register"),
]
