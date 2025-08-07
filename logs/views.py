from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import (
    LogSerializer,
    ZoneConnectionSerializer,
    LogListSerializer,
    LogUpdateSerializer,
    ZoneConnectionListSerializer,
)
from .models import Log, ZoneConnection
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from random import randint
# import time


class LogCreate(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]
    # number_count = 0

    # def randomValidate(self):
    #     random_number = randint(1, 100)
    #     if random_number % 2 == 0:
    #         if self.__class__.number_count < 3:
    #             self.__class__.number_count += 1
    #             time.sleep(10)
    #             return True
    #         else:
    #             self.__class__.number_count = 0
    #             return False
    #     else:
    #         self.__class__.number_count = 0
    #         return True

    # def puzzle(self):
    #     pass

    @swagger_auto_schema(security=[{"Token": []}])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
        # result = self.randomValidate()
        # if result:
        #     return super().post(request, *args, **kwargs)
        # if self.puzzle():
        #     return super().post(request, *args, **kwargs)


class LogList(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogListSerializer


class LogUpdate(generics.UpdateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogUpdateSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["patch", "put"]

    @swagger_auto_schema(security=[{"Token": []}])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(security=[{"Token": []}])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class LogDelete(generics.DestroyAPIView):
    lookup_field = "pk"
    queryset = Log.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(security=[{"Token": []}])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ZoneConnectionCreate(generics.CreateAPIView):
    queryset = ZoneConnection.objects.all()
    serializer_class = ZoneConnectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(security=[{"Token": []}])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ZoneConnectionList(generics.ListAPIView):
    queryset = ZoneConnection.objects.all()
    serializer_class = ZoneConnectionListSerializer
