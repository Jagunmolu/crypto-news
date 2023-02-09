from rest_framework import serializers

from news.models import Post


class PostListSerializer(serializers.ModelSerializer):
    # timesince = serializers.DateTimeField()
    class Meta:
        model = Post
        exclude = ('content',)
        # fields = ['title', 'image', 'post_category']
        # fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    # timesince = serializers.DateTimeField()
    class Meta:
        model = Post
        # fields = ['title', 'image', 'post_category']
        fields = '__all__'
