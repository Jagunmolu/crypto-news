from rest_framework import serializers

from guide.models import Guide


class GuideListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guide
        exclude = ('content',)


class GuideDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guide
        fields = '__all__'
