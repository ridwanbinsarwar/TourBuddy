from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from profiles.models import UserProfile
from django.http import HttpResponse
from rest_framework import status
from tourBuddyAPI.serializers import UserProfileSerializer
from rest_framework.response import Response
from accounts.models import User
import json


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JSONWebTokenAuthentication]

    def get_object(self, user):
        try:
            return UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        user = User.objects.get(email=request.user)  # get user(accounts app)
        profile = self.get_object(user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(email=request.user)  # get user(accounts app)
        profile = self.get_object(user)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = User.objects.get(email=request.user)  # get user(accounts app)
        profile = self.get_object(user)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
