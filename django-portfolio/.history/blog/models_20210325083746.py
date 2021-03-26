from django.db import models
from django.template.defaultfilters import truncatechars

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

# def __str__(self):  
#   return self.title

  
def summary(self):
    return {{self.content|truncatechars:100}}

# def pub_date_pretty(self):
#   return self.pub_date.strftime('%b %e %Y')