from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=35)
    author = models.CharField(max_length=20)
    description = models.TextField()
    pages = models.IntegerField()
    is_new = models.BooleanField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

