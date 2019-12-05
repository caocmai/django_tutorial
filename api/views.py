# from django.shortcuts import render

# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# from polls.models import Question, Choice
# from api.serializers import QuestionSerializer
# from api.serializers import ChoiceSerializer

# class QuestionList(APIView):
#     def get(self, request):
#         questions = Question.objects.all()[:20] # Get the last 20 [start:end]
#         data = QuestionSerializer(questions, many=True).data # many=True beacuse many, then convert to JSON
#         return Response(data)

# class QuestionDetail(APIView):
#     def get(self, request, pk):
#         question = get_object_or_404(Question, pk=pk) # Get key or id from the URL, pk=id, AKA
#         data = QuestionSerializer(question).data
#         return Response(data)

#===================================================================================

# To simplyfy the code in views.py(optional)
# ListCreate, it lists and creates as one because you are doing it on one object
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from polls.models import Question
from api.serializers import QuestionSerializer
from api.serializers import ChoiceSerializer

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
