from django.shortcuts import render, redirect
from blog import services
from blog.models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):

    token = services.get_token_from_request(request)
    # print(token, request.user)
    if token == "unauthorized":
        # user not logged in , redirect user to login page
        return redirect('login_view')

    # receives all post in json format
    posts = services.get_post_by_user(token, "ALL")

    return render(request, 'post_list.html', {'posts': posts})


def new_post(request):
    token = services.get_token_from_request(request)

    if token == "unauthorized":
        # user not logged in , redirect user to login page
        return redirect('login_view')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.session['user']
            # post.published_date = timezone.now()

            services.upload_post(post, token)
            return redirect('post_list')

    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def view_post(request, id):
    post = services.view_post_api(id)
    return render(request, 'view_post.html', {'post': post})


def delete_post(request, id):
    token = services.get_token_from_request(request)

    if token == "unauthorized":
        # user not logged in , redirect user to login page
        return redirect('login_view')
    response = services.delete_post_api(id, token)
    return redirect('post_list')


def update_post(request, id):
    token = services.get_token_from_request(request)

    if token == "unauthorized":
        # user not logged in , redirect user to login page
        return redirect('login_view')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            response = services.update_post_api(post, id, token)
            print(response)
            return redirect('view_post', id=id)
    else:
        item = services.view_post_api(id)
        print(type(item))
        form = PostForm(item)
    return render(request, 'update_post.html', {'form': form})


def post_list_by_user(request):

    token = services.get_token_from_request(request)
    if token == "unauthorized":
        # user not logged in , redirect user to login page
        return redirect('login_view')

    # receives all post in json format
    posts = services.get_post_by_user(token, request.session['user'])
    print(posts)
    return render(request, 'post_list.html', {'posts': posts})
