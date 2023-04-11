from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # blog post model
    title = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_area = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True)
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tags')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Commentary(models.Model):
    # post commentary model
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text[:50] + '...'

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "commentaries"


class Category(models.Model):
    # blog category model
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tags(models.Model):
    # post tags model
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
