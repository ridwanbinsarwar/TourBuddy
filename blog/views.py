from django.shortcuts import render, redirect
from blog import services
from blog.models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = services.get_all_post(request.headers.get('Authorization'))  # receives all post in json format
    print("---------------", posts, request.headers.get('Authorization'))
    return render(request, 'post_list.html', {'posts': posts})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()

            services.upload_post(post)
            return redirect('post_list')

    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def view_post(request, id):
    post = services.view_post_api(id)
    return render(request, 'view_post.html', {'post': post})


def delete_post(request, id):
    response = services.delete_post_api(id)
    return redirect('post_list')


def update_post(request, id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            response = services.update_post_api(post, id)
            print(response)
            return redirect('view_post', id=id)
    else:
        item = services.view_post_api(id)
        print(type(item))
        form = PostForm(item)
    return render(request, 'update_post.html', {'form': form})
