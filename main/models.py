from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news/img")

    def __str__(self):
      return self.title




