from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import TestSerializer, QuestionSerializer, AnswerSerializer, VariantSerializer

from .models import Data, Test, Question, Answer, Variant


def hello_world(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        data = Data(text=text)
        data.save()
        return HttpResponse("Saved!")
    texts = Data.objects.values_list('text')
    texts_array = list(texts)
    return JsonResponse(texts_array, safe=False)

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class VariantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
