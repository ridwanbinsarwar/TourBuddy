from django.shortcuts import render, redirect
import blog.services
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = blog.services.get_all_post()  # receives all post in json format
    return render(request, 'post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()

            blog.services.upload_post(post)

    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
