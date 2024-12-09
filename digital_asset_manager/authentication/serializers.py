from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Asset, Category


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class AssetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Asset
        fields = ['id', 'user', 'category', 'category_name', 'title', 'description', 'file', 'created_at', 'updated_at']
