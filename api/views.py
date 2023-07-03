from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TestSerializer, QuestionSerializer, OptionSerializer

from .models import Data, Test, Question, Option


def hello_world(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        data = Data(text=text)
        data.save()
        return HttpResponse("Saved!")
    texts = Data.objects.values_list('text')
    texts_array = list(texts)
    return JsonResponse(texts_array, safe=False)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['test']

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
