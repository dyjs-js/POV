from django.contrib import admin
from .models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "director",
        "cast",
        "is_public",
    )
    search_fields = ("title",)
    list_filter = ("is_public",)
    list_editable = ("is_public",)
