from django.db import models


class Author(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  def __str__(self):
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  publication_date = models.DateField(null=True, blank=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "books",
    null=True,
    blank=True)
  def __str__(self):
    return self.title