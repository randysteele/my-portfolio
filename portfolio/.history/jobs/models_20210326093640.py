from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=1000)
    heroku_url = models.URLField(max_length=100, null=True)
    github_url = models.URLField(max_length=100, null=True)


