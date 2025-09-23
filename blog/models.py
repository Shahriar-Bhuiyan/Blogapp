from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    liked_user = models.ManyToManyField(User, related_name='liked_posts')
    
    def __str__(self):
          return self.title

class Comment (models.Model):
     content = models.TextField()
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     post = models.ForeignKey(Post,on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return self.user.name