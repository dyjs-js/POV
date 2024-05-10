from django.contrib import admin
from .models import GptPhoto


# Register your models here.
@admin.register(GptPhoto)
class GptPhotoAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "movie")
