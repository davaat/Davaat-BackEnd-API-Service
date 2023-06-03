from authentication.models import User
from signature.models import Signature
from contract.models import Contract, Questionnaire, Question, Category, ContractFile
from django.http import JsonResponse
from .serializers import ContractSerializer, QuestionnaireSerializer, QuestionSerializer, CatSerializer, ContractlibrarySerializer
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
import mammoth




class UserQuestionnaireList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):

        query = Questionnaire.objects.filter(creator=request.user)
        query_serializer = QuestionnaireSerializer(query, many=True)

        ''' 
        for Q in query:
            questions = Question.objects.filter(questionnaire=Q)
            question_serializer = QuestionSerializer(questions, many=True)
            q_serializer = QuestionnaireSerializer(Q, many=True)

            print('---------')
            print(question_serializer)
            print(q_serializer)
        print('----------------')

            #questionnaire_obj = {'Questionnaire':q_serializer,'questions':question_serializer }
            #list.append(questionnaire_obj)
        '''
        return Response(query_serializer.data, status=status.HTTP_200_OK)



class AddQuestionnaire(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        try:
            questionnaire = Questionnaire()
            questionnaire.creator = User.objects.get(id=request.user.id)
            questionnaire.contract = Contract.objects.get(id=data['contract'])
            questionnaire.save()

            question = Question()
            question.questionnaire = Questionnaire.objects.get(id=questionnaire.id)
            for q in data['questions']:
                question.question = q
            question.save()
            return Response('questionnaire create successfully', status=status.HTTP_201_CREATED)
        except:
            return Response('something went wrong please try again', status=status.HTTP_400_BAD_REQUEST)





class AddCat(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        data['creator_company'] = request.user.id
        serializer = CatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Catlist(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        query = Category.objects.all()
        serializer = CatSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Contractlibrary(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        try:
            query = ContractFile.objects.filter(uploader=User.objects.get(id=request.user.id))
            serializer = ContractlibrarySerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response('library for this user not found something went wrong', status=status.HTTP_400_BAD_REQUEST)




class AddContractLibrary(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        data['uploader'] = request.user.id
        serializer = ContractlibrarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





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

        #document = Document(data['file'])
        #print(document._body._body.xml)

        result = mammoth.convert_to_html(data['file'])
        html = result.value  # The generated HTML
        messages = result.messages  # Any messages, such as warnings during conversion

        return Response(html, status=status.HTTP_200_OK)


    # https://stackabuse.com/how-to-convert-docx-to-html-with-python-mammoth/
    # https://pypi.org/project/docx2html/
    # https://npmdoc.github.io/node-npmdoc-mammoth/build/apidoc.html


