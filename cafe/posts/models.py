from django.db import models


# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    messege = models.TextField()
    time = models.DateTimeField(auto_now_add=True,auto_now=False)
    
    def __unicode__(self):
        return self.email
    def __str__(self):
        return self.email

