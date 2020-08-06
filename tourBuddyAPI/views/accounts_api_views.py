from rest_framework.views import APIView
from rest_framework.response import Response
from tourBuddyAPI.serializers import RegistrationSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.contrib import auth
from profiles.models import UserProfile
from accounts.models import User


# view to get all Post and add new Post
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            # create a UserProfile associated with the registered account
            UserProfile.objects.create(
                user=account,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
            'email': serializer.data['email'],
        }
        status_code = status.HTTP_200_OK
        # if authentication is successful , get user object by email and login
        # auth.login(request, User.objects.get(serializer.data['email']))
        return Response(response, status=status_code)
