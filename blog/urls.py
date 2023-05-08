"""
List of URL patterns for the 'blog' app.

Each URL pattern is a `path` object that maps a URL to a view function.


URL Patterns:
- `blog/`: Displays a list of all blog posts using the `blog` view function.
- `post/<int:pk>`: Displays a single blog post specified by the primary key `pk`
   using the `post` view function.
"""
from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('post/<int:pk>', post, name='post'),
]
