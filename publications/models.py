from django.db import models

class Publications(models.Model):
    pub_year = models.DateField()
    pub_title = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    pub_body = models.CharField(max_length=200)
    pub_type = models.CharField(max_length=200)
    pub_doi = models.URLField()


    def publication_date_short(self):
        # https://strftime.org 
        return self.pub_year.strftime('%Y')

    def __str__(self):
        return self.pub_title