from django.contrib import admin
from .models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "user",
        "is_public",
        "rating",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "author",
        "user__username",
    )
    list_filter = ("is_public",)
    list_editable = ("is_public",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )
