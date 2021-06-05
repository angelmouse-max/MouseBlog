from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.text

class Comment(models.Model):
    blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text