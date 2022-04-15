from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import routers
from django.urls import path
from django.contrib import admin
import random


class Random0to100ViewSet(GenericViewSet):
    def list(self, request):
        return Response(random.randint(0, 100))


router = routers.DefaultRouter()
router.register("random0to100", Random0to100ViewSet, basename="random0to100")


urlpatterns = router.urls
urlpatterns += [
    path("admin/", admin.site.urls),
]
