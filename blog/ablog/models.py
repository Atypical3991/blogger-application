from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url=models.CharField(max_length=255,null=True,blank=True)
    facebook_url=models.CharField(max_length=255,null=True,blank=True)
    instagram_url=models.CharField(max_length=255,null=True,blank=True)
    twitter_url=models.CharField(max_length=255,null=True,blank=True)
    pinterest_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return  str(self.user)



class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=255,default="")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255,default="coding")
    snippet = models.CharField(max_length=255,default="Snippet missing!! click on title to read the blog.")
    body = RichTextField(blank=True, null=True)
    # body=models.TextField()
    blog_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('article-detail',args=([self.id]))