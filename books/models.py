from django.db import models
from django.conf import settings
from common.models import CommonModel

# Create your models here.


class Book(CommonModel):
    """Model Definition for books"""

    review_title = models.CharField(
        max_length=100,
    )

    title = models.CharField(
        max_length=100,
    )
    author = models.CharField(
        max_length=100,
    )
    publisher = models.CharField(
        max_length=100,
        blank=True,
    )
    content = models.TextField()

    summary = models.TextField()
    image = models.ImageField(blank=True)
    is_public = models.BooleanField(
        verbose_name="is Public?",
        default=True,
        help_text="Does this reivew allow public?",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books",
    )

    def __str__(self):
        return self.review_title
