from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

class Secretarie(models.Model):
    name = models.CharField(max_length=50)
    USER_TYPE_CHOICES=(('1st','GENERAL SECRETARY'),('2nd','JOINT SECRETARY'))
    post = models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='2nd')
    #Image = models.FileField(blank=True)
    Image = models.FileField(blank=True)
    fb_link=models.URLField(max_length=50)
    git_link=models.URLField(max_length=50)
    linkedin_link=models.URLField(max_length=50)

class About_us(models.Model):
    #text=models.TextField(blank=True)
    Img=models.FileField(blank=True)
    #def __str__(self):
    #    return self.text+"-"+self.Img

class About_us_content(models.Model):
    content = models.TextField()
    display = models.BooleanField(default=False)


class Events(models.Model):
    logo=models.FileField(blank=True)
    heading=models.CharField(max_length=30)
    description=models.TextField(blank=True)
    USER_TYPE_CHOICES=(('msweek','MS Week'),('inspirus','Inspirus'),('rumble','Rumble'))
    type=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='msweek')


class MSWEEK_gallery(models.Model):
    caption=models.TextField(blank=True)
    Image=models.FileField(blank=True)
    timestamp=models.DateTimeField(auto_now=True)

class INSPIRUSUS_gallery(models.Model):
    caption=models.TextField(blank=True)
    Image=models.FileField(blank=True)
    timestamp=models.DateTimeField(auto_now=True)

class RUMBLE_gallery(models.Model):
    caption=models.TextField(blank=True)
    Image=models.FileField(blank=True)
    timestamp=models.DateTimeField(auto_now=True)

class index_gallery(models.Model):
    Image=models.FileField(blank=True)

class Team(models.Model):
    image=models.FileField(blank=True)
    name=models.CharField(max_length=50)
    USER_TYPE_CHOICES=(('1st','Technical'),('2nd','Event-Management'),('3rd','Creativity'),('4th','Publicity'))
    department=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='4th')

class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(null=True,blank=True)
    name = models.CharField(max_length=200,default=" ")
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    
    content=models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('newsfeed-detail',kwargs={'pk': self.pk})

    def __str__(self):
        return (self.title)

    class Meta:
        ordering = ["-timestamp"]


class MSWeek_Event(models.Model):
    title = models.CharField(max_length=100)
    poster = models.FileField()
    register_link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False,auto_now_add=False)
    description = models.TextField(null=True)

class Inspirus_Event(models.Model):
    title = models.CharField(max_length=100)
    poster = models.FileField()
    register_link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False,auto_now_add=False)
    description = models.TextField(null=True)
    
class Rumble_Event(models.Model):
    title = models.CharField(max_length=100)
    poster = models.FileField()
    register_link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False,auto_now_add=False)
    description = models.TextField(null=True)
    
