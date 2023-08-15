from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,)

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'phone_number',
            'date_of_birth',
        )

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
        )
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
            'phone_number',
            'last_name',
            'first_name',
            'date_of_birth',
        )
