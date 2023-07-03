from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TestSerializer

from .models import Data, Test


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
