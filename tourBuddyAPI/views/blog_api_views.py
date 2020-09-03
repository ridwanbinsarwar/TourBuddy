from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from tourBuddyAPI.serializers import PostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from accounts.models import User


# Create your views here.

# view to get all Post and add new Post
class ArticleAPIView(APIView):
    # permission_classes = (AllowAny,)

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):

        if request.data['user'] == 'ALL':
            posts = Post.objects.all()
        else:
            uid = User.objects.get(email=request.data['user']).id
            posts = Post.objects.all().filter(author=uid)
        serializer = PostSerializer(posts, many='True')
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = User.objects.get(email=request.user).id
        print(request.data)
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to get/update/delete specific post
class ArticleDetails(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_object(id)
        request.data['author'] = User.objects.get(email=request.user).id
        if request.user != post.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = self.get_object(id)
        if request.user != post.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

