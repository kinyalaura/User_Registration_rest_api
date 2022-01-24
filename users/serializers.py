from distutils.command.build_scripts import first_line_re
import email
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length =65, min_length = 8, write_only = True)
    email = serializers.EmailField(max_length = 255, min_length = 4)
    first_name  =serializers.CharField(max_length = 255, min_length = 2)
    last_name = serializers.CharField(max_length = 255, min_length = 2)
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']
        
    def validate(self, data):
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})
        return data

    def create(self, validated_data):
        return UserModel.objects.create_user(
            email = validated_data['email'],
            first_name =validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password']
        )