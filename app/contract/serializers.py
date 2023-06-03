from rest_framework import serializers
from .models import Contract, Questionnaire, Question, Category, ContractFile


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ContractlibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractFile
        fields = '__all__'