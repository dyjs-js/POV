from django.contrib import admin
from .models import Photo, Video

# Register your models here.


def delete_selected(modeladmin, request, queryset):
    queryset.delete()


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "movie")
    action = [delete_selected]
    actions_on_top = True
    actions = [delete_selected]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
