from django.urls import path
from . import views

urlpatterns = [
    path("", views.Books.as_view()),
    path("<int:pk>", views.BookDetail.as_view()),
]
