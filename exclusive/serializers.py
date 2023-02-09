from django.contrib.auth.models import User
from rest_framework import serializers

from exclusive.models import Exclusive


class ExclusiveListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Exclusive
        exclude = ('content',)


class ExclusiveDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Exclusive
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    exclusives = serializers.PrimaryKeyRelatedField(many=True, queryset=Exclusive.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'exclusives']
