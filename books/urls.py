from django.urls import path
from . import views

urlpatterns = [
    path("", views.Books.as_view()),
    path("<int:pk>", views.BookDetail.as_view()),
    path("<int:pk>/liked", views.BookLiked.as_view()),
    path("<int:pk>/photos", views.BookPhotos.as_view()),
]
