from rest_framework import serializers

from exclusive.models import Exclusive


class ExclusiveListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exclusive
        exclude = ('content',)


class ExclusiveDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exclusive
        fields = '__all__'
