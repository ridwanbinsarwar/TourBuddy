from django.shortcuts import render
import blog.services


# Create your views here.
def post_list(request):
    posts = blog.services.get_all_post()  # receives all post in json format
    return render(request, 'post_list.html', {'posts': posts})
