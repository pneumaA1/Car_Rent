from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from blog.models import Post, Commentary, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_objs = paginator.get_page(page_number)

    context = {"page_objs": page_objs}
    return render(request, 'blog/blog.html', context=context)


def post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Commentary.objects.filter(post_id=pk)
    categories = Category.objects.annotate(num_posts=Count('post'))
    context = {
        'post': post,
        'comments': comments,
        'categories': categories
    }
    return render(request, 'blog/post.html', context)