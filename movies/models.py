from django.db import models


# Create your models here.
class Movie(models.Model):
    """Model Definition for movies"""

    review_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100, blank=True)
    cast = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    summary = models.TextField()
    is_public = models.BooleanField(
        verbose_name="is Public?",
        default=True,
        help_text="Does this reivew allow public?",
    )

    def __str__(self):
        return self.review_title
