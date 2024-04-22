from django.contrib import admin
from .models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "is_public",
    )
    search_fields = ("title",)
    list_filter = ("is_public",)
    list_editable = ("is_public",)
