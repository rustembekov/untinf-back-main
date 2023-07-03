from .views import hello_world
from django.urls import include, path
from rest_framework import routers

from .views import TestViewSet, QuestionViewSet, AnswerViewSet, VariantViewSet

router = routers.DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'variants', VariantViewSet)

urlpatterns = [
    path('data/', hello_world),
    path('api/', include(router.urls)),
]
