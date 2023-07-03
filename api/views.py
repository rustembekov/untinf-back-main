import random

from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from .serializers import TestSerializer, QuestionSerializer, OptionSerializer
from rest_framework.response import Response
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
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['test']
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        questions = Question.objects.all()
        random_questions = random.sample(list(questions), len(questions))
        return random_questions


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        all_options = list(Option.objects.all())
        random.shuffle(all_options)
        serializer = self.get_serializer(all_options, many=True)
        return Response(serializer.data)
