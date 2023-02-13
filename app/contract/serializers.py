from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=256, allow_null=False)
    password = serializers.CharField(max_length=256, allow_null=False)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password', 'is_driver', 'national_code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        exclude = ['password']


class ConfirmationSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=5, allow_null=False)
