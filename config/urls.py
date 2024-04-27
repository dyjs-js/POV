from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
]
