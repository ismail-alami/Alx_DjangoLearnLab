from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager




class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    # Add any additional fields you need

    def _str_(self):
        return self.user.username
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who created the post

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)  # Link to the Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    content = models.TextField()  # The comment text
    created_at = models.DateTimeField(default=timezone.now)  # Time the comment was created
    updated_at = models.DateTimeField(auto_now=True)  # Time the comment was last updated

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()  # Add tags to the Post model

    def __str__(self):
        return self.title