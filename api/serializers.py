# Changes from model to json and back using this serializers
from rest_framework.serializers import ModelSerializer

from polls.models import Question, Choice

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__' # Want all fields in model to be serialized

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice # Only this changes and class name
        fields = '__all__'
