from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()
    image_path = models.CharField(max_length=300)

    def __str__(self):
        return self.title

