from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from .models import Review, Rating


class ReviewSerializer(serializers.ModelSerializer):
    content_type_name = serializers.CharField(write_only=True)

    def create(self, validated_data):
        content_type_name = validated_data.pop('content_type_name')
        content_type = ContentType.objects.get(model=content_type_name)
        validated_data['content_type'] = content_type
        return super().create(validated_data)

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'author',
            'content_type_name',
            'object_id'
        )
        read_only_fields = (
            'id',
            'author',
        )


class RatingSerializer(serializers.ModelSerializer):
    content_type_name = serializers.CharField(write_only=True)

    def create(self, validated_data):
        content_type_name = validated_data.pop('content_type_name')
        content_type = ContentType.objects.get(model=content_type_name)
        validated_data['content_type'] = content_type
        return super().create(validated_data)

    class Meta:
        model = Rating
        fields = (
            'id',
            'user',
            'content_type_name',
            'object_id',
            'rating_value',
        )
        read_only_fields = (
            'id',
            'user',
        )
