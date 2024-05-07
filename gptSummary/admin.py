from django.contrib import admin
from .models import GptSummaryModel


@admin.register(GptSummaryModel)
class GptSummaryAdmin(admin.ModelAdmin):
    pass
