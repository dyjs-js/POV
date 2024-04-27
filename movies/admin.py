from django.contrib import admin
from .models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "director",
        "cast",
        "user",
        "is_public",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "director",
        "user__username",
    )
    list_filter = ("is_public",)
    list_editable = ("is_public",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )
