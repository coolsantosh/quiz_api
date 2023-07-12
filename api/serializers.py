from rest_framework import serializers
from .models import *






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= "__all__"




class QuizSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model= Quiz
        exclude= ['answer']
