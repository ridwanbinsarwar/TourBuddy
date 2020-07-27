from rest_framework import serializers
from profiles.models import UserProfile
from accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'age', 'gender')


# class UserProfileSerializer(serializers.Serializer):
#     profile = UserSerializer(required=False)
#
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'profile')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validate_data):
#         profile_data = validate_data.pop('profile')
#         user = User.objects.create_user(**validate_data)
#         UserProfile.objects.create(
#             user=user,
#             first_name=profile_data['first_name'],
#             last_name=profile_data['last_name'],
#             phone_number=profile_data['phone_number'],
#             age=profile_data['age'],
#             gender=profile_data['gender']
#         )
#
#         return user
