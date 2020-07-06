from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # select every attribute of model
        # use fields =[ 'name' ] for custom
