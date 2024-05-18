from django.contrib import admin
from .models import GptPhoto, GptHashtag


# Register your models here.
@admin.register(GptPhoto)
class GptPhotoAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "movie")


@admin.register(GptHashtag)
class GptHashtagAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "movie")
