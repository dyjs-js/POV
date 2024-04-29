from django.urls import path
from . import views


urlpatterns = [
    path("", views.Movies.as_view()),
    path("<int:pk>", views.MovieDetail.as_view()),
    path("<int:pk>/liked", views.MovieLiked.as_view()),
    path("<int:pk>/photos", views.MoviePhotos.as_view()),
]
