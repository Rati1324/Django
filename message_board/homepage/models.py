from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title= models.CharField(max_length=30,null=True,blank=True)
    body= models.TextField(max_length=500)
    date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    comments_amount=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    body = models.TextField(max_length=100,null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None,null=True,blank=True)
    id_post=models.CharField(max_length=10,default=None,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    # def __str__(self):
    #     return self.body