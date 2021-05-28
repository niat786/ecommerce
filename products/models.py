from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    description = models.TextField()
    price = models.CharField(max_length=20)
    body = models.TextField()
    tags = models.CharField(max_length=50)
    keywords = models.CharField(max_length=40)
    images = models.ImageField(default='blank.jpg', blank=True)
    author = models.ForeignKey(User, default=None,  on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name