from rest_framework import serializers

from .models import CultureCategory, Culture


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class CultureCategorySerializer(serializers.ModelSerializer):
    cultures = CultureSerializer(many=True, read_only=True)

    class Meta:
        model = CultureCategory
        fields = '__all__'


class CultureCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureCategory
        fields = '__all__'

