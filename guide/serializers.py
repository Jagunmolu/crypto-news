from rest_framework import serializers
from django.contrib.auth.models import User

from guide.models import Guide


class GuideListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Guide
        exclude = ('content',)


class GuideDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Guide
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    guides = serializers.PrimaryKeyRelatedField(many=True, queryset=Guide.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'guides']
