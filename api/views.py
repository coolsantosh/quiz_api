from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class CategoryView(APIView):
    def get(self,request):
        queryset=Category.objects.all()

        serializers = CategorySerializer(queryset,many=True)

        return Response({"data":serializers.data})







class QuizView(APIView):
    def get(self, request):
        category_name = request.query_params.get("category_name", None)
        if category_name:
            querySet = Quiz.objects.filter(category__name=category_name)
        else:
            querySet = Quiz.objects.all()
        serializer = QuizSerializer(querySet, many=True)
        return Response({"data": serializer.data},status=status.HTTP_200_OK)
    
    # querySet = Quiz.objects.all()
    # serializer_class = QuizSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category__name']
   
    # def get(self):
    #     data =  Quiz.objects.all()
    #     return Response({"data": data},status=status.HTTP_200_OK)
    
    def post(self, request):
        answerByUser = request.data.get("user_answer")
        questionId = request.data.get("question_id")

        try:
            queryset = Quiz.objects.get(id=questionId)

            if queryset.answer == answerByUser:
                return Response(
                    {"message": "Correct Answer"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "Incorrect Answer"}, status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response(
                {"mesasage": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
