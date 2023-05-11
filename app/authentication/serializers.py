from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=256, allow_null=False)
    password = serializers.CharField(max_length=256, allow_null=False)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        exclude = ['password']


class ConfirmationSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=5, allow_null=False)



class RequestOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=64, allow_null=False)


class ConfirmationOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=64, allow_null=False)
    otp = serializers.CharField(max_length=5, allow_null=False)


class ResetPassOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=64, allow_null=False)
    otp = serializers.CharField(max_length=5, allow_null=False)
    password = serializers.CharField(max_length=64, allow_null=False)




class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=64, allow_null=False)
    national_code = serializers.CharField(max_length=64, allow_null=False)
