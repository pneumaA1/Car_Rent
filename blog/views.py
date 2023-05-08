from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from blog.models import Post, Commentary, Category
from blog.forms import CommentForm


def blog(request):
    """
        View function that retrieves all posts from the database, paginates them with 3 posts per page,
        and renders a blog page with the paginated posts. The current page number is obtained from the
        'page' query parameter in the request. If the requested page number is invalid, the first page
        is displayed. The context dictionary passed to the template includes the Page object for the
        current page, which provides access to the list of posts and information about pagination.
    """
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_objs = paginator.get_page(page_number)

    context = {"page_objs": page_objs}
    return render(request, 'blog/blog.html', context=context)


def post(request, pk):
    """
       This function handles both GET and POST requests for a particular blog post along with its comments and categories.
    """
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
