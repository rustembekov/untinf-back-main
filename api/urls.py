from .views import hello_world
from django.urls import include, path
from rest_framework import routers

from .views import TestViewSet


router = routers.DefaultRouter()
router.register(r'tests', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
