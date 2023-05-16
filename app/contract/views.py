from authentication.models import User
from signature.models import Signature
from contract.models import Contract
#from django.http import JsonResponse
from .serializers import ContractSerializer
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
import docx2txt
from docx import Document



class ContractLists(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        query = Contract.objects.filter(user=request.user)
        serializer = ContractSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class AddContract(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        data['user'] = request.user.id
        serializer = ContractSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UploadContract(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        data['user'] = request.user.id

        #TEXT = docx2txt.process(data['file'])

        document = Document(data['file'])
        print(document._body._body.xml)


        return Response(document._body._body.xml, status=status.HTTP_200_OK)
        #serializer = ContractSerializer(data=data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

