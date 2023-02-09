from rest_framework import serializers
from django.contrib.auth.models import User

from news.models import Post


class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # timesince = serializers.DateTimeField()
    class Meta:
        model = Post
        exclude = ('content',)
        # fields = ['title', 'image', 'post_category']
        # fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # timesince = serializers.DateTimeField()
    class Meta:
        model = Post
        # fields = ['title', 'image', 'post_category']
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
