from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField
    pub_date = models.DateField
    content = models.TextField
    image = models.ImageField(upload_to='images/')
    

