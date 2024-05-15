from django.urls import path
from .views import GetUploadGPTURL, GPTPhotoDetail

urlpatterns = [
    path("gptphotos/get-url", GetUploadGPTURL.as_view()),
    path("gptphotos/<int:pk>", GPTPhotoDetail.as_view()),
]
