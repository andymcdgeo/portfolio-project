from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    blog_text = models.TextField()
    image = models.ImageField(upload_to='images/')