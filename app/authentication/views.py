from .models import User
#from django.http import JsonResponse
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, ConfirmationSerializer, ResetPassOTPSerializer, RequestOTPSerializer, ConfirmationOTPSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status, pagination, mixins
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from . import helper





class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data = serializer.errors)

        try:
            phone = data['phone']
            user = User.objects.get(phone=phone)

            if helper.check_send_otp(user.phone):
                # send otp
                otp = helper.get_random_otp()
                print(otp)
                helper.otpsend(phone, otp)
                #helper.send_otp_soap(mobile, otp)

                user.otp = otp
                user.save()
                return Response('کد تایید به شماره {} ارسال شد'.format(data['phone']) , status=status.HTTP_200_OK)
            else:
                return Response('کد ارسال شده، لطفا ۲ دقیقه دیگر اقدام نمایید' , status=status.HTTP_408_REQUEST_TIMEOUT)

        except User.DoesNotExist:
            return Response('کاربری با شماره {} یافت نشد، لطفا ثبت نام کنید'.format(data['phone']) , status=status.HTTP_400_BAD_REQUEST)



class CompanyLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        try:
            user = authenticate(request, email=data['email'], password=data['password'])
            login(request, user)
            token = RefreshToken.for_user(user)
            token_response = { "refresh": str(token), "access": str(token.access_token) }
            response = { 'token':token_response , 'user':UserSerializer(user).data }
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response('email or password is incorrect', status=status.HTTP_406_NOT_ACCEPTABLE)





class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
            return Response('User Logged out successfully', status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response('Error in logout', status=status.HTTP_400_BAD_REQUEST)




class UserRegister(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        if User.objects.filter(is_company=True, invitation_referral=data['referral']).exists():
            data['is_company'] = False
            password = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
            data['password'] = password
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                data = serializer.validated_data
                serializer.save()
                user = User.objects.get(phone=data['phone'])
                otp = helper.get_random_otp()
                helper.otpsend(user.phone, otp)
                print(otp)
                user.otp = otp
                user.otp_create_time = timezone.now()
                user.save()
                return Response('کد تایید به شماره {} ارسال شد'.format(user.phone), status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        else:
            return Response("invitation referral not found or somting wrong, please try again.", status=status.HTTP_400_BAD_REQUEST)





class CompanyRegister(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        data['is_company'] = True
        password = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        data['password'] = password
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            serializer.save()
            user = User.objects.get(email=data['email'])
            user.set_password(password)
            user.save(update_fields=['password'])
            print(password)

            if helper.email_send_code(user, password):
                email_msg = "password send to {}".format(user.email)
            else:
                email_msg = "Error sending email - Please try again!"

            return Response(email_msg, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)




class OTPConfirmation(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ConfirmationOTPSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        user = User.objects.get(phone=data['phone'])
        otp = data['otp']

        if user.otp != int(otp):
            return Response(data="کد اشتباه است", status=status.HTTP_417_EXPECTATION_FAILED)
        user.is_active = True
        user.otp_confirmed = True
        user.save()
        login(request, user)
        token = RefreshToken.for_user(user)
        token_response = {"refresh": str(token), "access": str(token.access_token)}
        response = {'token': token_response, 'user': UserSerializer(user).data}
        return Response(response, status=status.HTTP_200_OK)








class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        profile = User.objects.get(id=request.user.id)
        serializer = UserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        profile = User.objects.get(id=request.user.id)
        data = request.data
        data['phone']=profile.phone
        data['password']=profile.password
        serializer = UserSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




#---------------------------------------------------- Confirmation -------------
class Confirmation(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data = serializer.errors)
        profile = User.objects.get(id=self.request.user.id)
        if data['code'] == str(profile.otp):
            profile.confirmed = True
            profile.save()
            token = RefreshToken.for_user(profile)
            token_response = { "refresh": str(token), "access": str(token.access_token) }
            response = { 'token':token_response , 'user':UserSerializer(profile).data }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response("User not verified", status=status.HTTP_406_NOT_ACCEPTABLE)





class ResetPass(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            phone = request.data['phone']
            user = User.objects.get(phone=phone)
            #send otp
            if helper.check_send_otp(user.phone):
                # send otp
                otp = helper.get_random_otp()
                print(otp)
                helper.otpsend(phone, otp)
                # helper.send_otp_soap(mobile, otp)
                user.otp = otp
                user.otp_create_time = timezone.now()
                user.save()
                return Response('کد تایید به شماره {} ارسال شد'.format(phone), status=status.HTTP_200_OK)
            else:
                return Response('کد ارسال شده، لطفا ۲ دقیقه دیگر اقدام نمایید', status=status.HTTP_408_REQUEST_TIMEOUT)
        except Exception as e:
            return Response("User not found or somting wrong, please try again. {}".format(e), status=status.HTTP_400_BAD_REQUEST)




class ResetPassConf(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ResetPassOTPSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data = serializer.errors)

        phone = data['phone']
        user = User.objects.get(phone=phone)
        otp = data['otp']
        password = data['password']

        # check otp expiration
        if not helper.check_otp_expiration(user.phone):
            return Response(data="کد منقضی شده است، لطفا دوباره امتحان کنید", status=status.HTTP_408_REQUEST_TIMEOUT)

        if user.otp != int(otp):
            return Response(data="کد اشتباه است", status=status.HTTP_417_EXPECTATION_FAILED)

        user.is_active = True
        user.set_password(password)
        user.save()

        return Response('password changed successfully', status=status.HTTP_200_OK)

