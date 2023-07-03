from rest_framework import  serializers

from api.models import Test, Question, Option


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
