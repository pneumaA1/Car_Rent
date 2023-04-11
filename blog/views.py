from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from blog.models import Post, Commentary, Category
from blog.forms import CommentForm


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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = post
            form.save()
    else:
        form = CommentForm()

    categories = Category.objects.annotate(num_posts=Count('post'))
    context = {
        'post': post,
        'comments': comments,
        'categories': categories,
        'form': form,
    }
    return render(request, 'blog/post.html', context)
