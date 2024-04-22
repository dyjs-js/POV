from django.db import models

# Create your models here.


class Book(models.Model):
    """Model Definition for books"""

    review_title = models.CharField(max_length=100)

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    publisher = models.CharField(max_length=100, blank=True)
    summary = models.TextField()
    is_public = models.BooleanField(
        verbose_name="is Public?",
        default=True,
        help_text="Does this reivew allow public?",
    )

    def __str__(self):
        return self.review_title
