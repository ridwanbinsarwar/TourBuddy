from rest_framework import serializers
from blog.models import Post
from accounts.models import Account
from profiles.models import UserProfile
from accounts.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # select every attribute of model
        # use fields =[ 'name' ] for custom


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'age', 'gender')


class RegistrationSerializer(serializers.ModelSerializer):
    # write_only set to TRUE so pass is encrypted
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})
        account.password = password
        account.save()
        return account

#
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import update_last_login
# from rest_framework_jwt.settings import api_settings
#
# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#
#
# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         print(email, password, Account.objects.get(email=email, password=password))
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password is not found.'
#             )
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             # update_last_login(None, user)
#         except Account.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#         return {
#             'email': user.email,
#             'token': jwt_token
#         }





