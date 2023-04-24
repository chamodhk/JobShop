
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

categories = [
    ("1","Information technology"),
    ("2","Education"),
    ("3","Accounting"),
    ("4","Other")
]


class Job(models.Model):
    title = models.CharField(max_length=256)
    employer = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=256)
    views = models.IntegerField(default=0)
    impressions = models.IntegerField(default=0)
    banner = models.ImageField(upload_to='banners/',blank=True)
    posted_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=3,choices=categories,default='1')
    tags = TaggableManager(blank=True)
    

    def __str__(self):
        return self.title
    
    def impressed(self):
        self.impressions += 1
        self.save()

    def viewed(self):
        self.views += 1
        self.save()
        return self.views

    def get_absolute_url(self):
        
        return reverse('job_view',args=[self.pk])
    
