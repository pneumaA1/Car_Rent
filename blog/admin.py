from django.contrib import admin

from blog.models import Post, Category, Commentary, Tags

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Commentary)
admin.site.register(Tags)