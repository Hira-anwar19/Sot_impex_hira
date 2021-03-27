from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=255)
    email =models.CharField(max_length=100)
    ph_no =models.CharField(max_length=13)
    message=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True, null=True)# this is contactus model

class Estimate(models.Model):
    name =models.CharField(max_length=255)
    email =models.CharField(max_length=100)
    ph_no =models.CharField(max_length=13)
    service=models.CharField(max_length=100) 
    message=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True,null=True)# this is contactus model

class Subscribe(models.Model):
    email =models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
)
def __str__(self):
    return self.title
    
def get_absolute_url(self):
    return reverse('comment_detail', args=[str(self.id)])

class Comment(models.Model): # new
    Blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    comment = models.TextField(max_length=140, null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog_list')

