from django.contrib import admin
from .models import Liked

# Register your models here.


@admin.register(Liked)
class LikedAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payload",
        "created_at",
        "book",
        "movie",
    )
