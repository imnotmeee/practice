from django.db import models

class Post(models.Model):
    body = models.TextField(max_length=500)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_created=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=200)    
