from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
      A model representing a blog post.

      Attributes:
          title (str): The title of the post, limited to 70 characters.
          created_at (datetime): The date and time at which the post was created, automatically set
              to the current date and time when the object is first saved.
          author (User): The user who created the post, referenced from the built-in Django User model.
          text_area (str): The main content of the post, as a text field.
          image (ImageField): An optional image associated with the post, uploaded to the `blog_images/`
              directory on the server.
          categories (ManyToManyField): A many-to-many relationship with the `Category` model, allowing
              the post to belong to multiple categories.
          tags (ManyToManyField): A many-to-many relationship with the `Tags` model, allowing the post
              to be tagged with multiple tags.

      Methods:
          __str__(): Returns the title of the post (used mostly for debugging and admin purposes).

      Meta:
          verbose_name (str): A human-readable name for the model in singular form.
          verbose_name_plural (str): A human-readable name for the model in plural form.
      """
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
    """
    A model representing a comment made by a user on a post.

    Attributes:
        text (str): The content of the comment.
        post (Post): The post that is being commented on.
        author (User): The user who wrote the comment.
        email (str): The email address of the user who wrote the comment.
        created_at (DateTime): The date and time when the comment was created.
"""
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text[:50] + '...'

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"


class Category(models.Model):
    """
       A model representing a category of blog posts.

       Attributes:
           title (str): The title of the category, up to 50 characters.

       Methods:
           __str__(): Returns a string representation of the category, which is its title.
       """
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tags(models.Model):
    """
       Model representing the tags for a blog post.

       Attributes:
           title (str): The title of the tag.

       Methods:
           __str__: Returns the string representation of the tag.

       Meta:
           verbose_name (str): The singular name for the model in the admin interface.
           verbose_name_plural (str): The plural name for the model in the admin interface.
       """
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
