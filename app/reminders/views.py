from authentication.models import User
from reminders.models import Reminder
#from django.http import JsonResponse
from .serializers import ReminderSerializer
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



class ReminderLists(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        query = Reminder.objects.filter(user=request.user)
        serializer = ReminderSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ReminderItem(mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    serializer_class = ReminderSerializer

    def get(self, request, *args, **kwargs):
        reminder = Reminder.objects.get(id=self.kwargs["id"])
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        reminder = Reminder.objects.get(id=self.kwargs["id"])
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        reminder = Reminder.objects.get(id=self.kwargs["id"])
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class AddReminder(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        data['user'] = request.user.id
        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

