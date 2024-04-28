from django.urls import path
from . import views


urlpatterns = [
    path("", views.Movies.as_view()),
    path("<int:pk>", views.MovieDetail.as_view()),
]
