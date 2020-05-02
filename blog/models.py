from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    blog_text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.blog_text[0:100]

    def publication_date_short(self):
        # https://strftime.org 
        return self.publication_date.strftime('%B %e %Y')

    def __str__(self):
        return self.title