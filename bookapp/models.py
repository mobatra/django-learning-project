from django.db import models

class Book(models.Model):
  book_name = models.CharField(max_length=20)
  release = models.IntegerField()
  auth_name = models.CharField(max_length=20)