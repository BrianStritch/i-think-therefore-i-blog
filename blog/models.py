from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# a tuple to define the status
STATUS = ((0, 'Draft'), (1, 'Published')) 


# this is the POSTS MODEL
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # this class gets created inside the Post class and the following class and variables 
    #    are known as helpers and help structure the data
    class Meta:
        ordering = ['-created_on']   # the minus sign orders in descending

    # add this next block to your projects as django says its "it's a  
    #     magic method that returns a string 
    #     representation of an object and it says you should define  
    #     it because the default isn't helpful at all."

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# This is the COMMENTS MODEL

class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']   # without the minus sign orders in ascending

    def __str__(self):
        return f"Comment {self.body} by {self.name}"







