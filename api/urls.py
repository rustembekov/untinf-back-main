from .views import hello_world, QuestionViewSet, TestViewSet
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
