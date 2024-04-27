from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_books),
    path("<int:book_id>", views.see_one_book),
]
