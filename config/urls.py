from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/books/", include("books.urls")),
    path("api/v1/movies/", include("movies.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
