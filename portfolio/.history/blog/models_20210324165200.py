from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

def __str__(self):  
  return f"{self.last_name}, {self.first_name}"
    
def summary(self):
    return self.content[:80]

def pub_date_pretty(self):
  return self.pub_date.strftime('%b %e %Y')