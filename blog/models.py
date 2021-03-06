from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User') 
    title = models.CharField(max_length=200) 
    text = models.TextField() 
    category = models.CharField(max_length=200)
    created_date = models.DateTimeField(default = timezone.now) 
    published_date = models.DateTimeField(blank=True, null=True)
    
    
    file = models.FileField(null=True)
    filetwo = models.ImageField(blank=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __unicode__(self):
        return self.title
        