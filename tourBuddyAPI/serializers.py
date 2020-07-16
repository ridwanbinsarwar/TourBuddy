from rest_framework import serializers
from blog.models import Post
from accounts.models import Account


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # select every attribute of model
        # use fields =[ 'name' ] for custom


class RegistrationSerializer(serializers.ModelSerializer):
    # write_only set to TRUE so pass is encrypted
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})
        account.password = password
        account.save()
        return account
