from django.db import models
from django.utils import dateformat


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()
    image_path = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def date_str(self):
        return dateformat.format(self.date, 'M d, Y • H:i')
