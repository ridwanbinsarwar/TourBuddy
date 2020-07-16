from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from tourBuddyAPI.serializers import RegistrationSerializer
from rest_framework import status


# view to get all Post and add new Post
class RegistrationAPIView(APIView):

    # def get(self, request):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many='True')
    #     return Response(serializer.data)

    def post(self, request):

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
