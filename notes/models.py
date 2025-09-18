from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class myBlogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class myComments(models.Model):
    blog = models.ForeignKey(myBlogs, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_date']



# Create your models here.
