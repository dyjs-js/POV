from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(max_length=140)
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    file = models.URLField()
    # movie는 한개의 동영상만 가질 수 있음
    movie = models.OneToOneField(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "Video File"
