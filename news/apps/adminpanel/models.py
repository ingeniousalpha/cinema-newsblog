from django.db import models


class Admin(models.Model):
    nickname = models.CharField(max_length=50)
    password = models.TextField(max_length=100)
