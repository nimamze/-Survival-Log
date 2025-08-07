from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import (
    ZoneSerializer,
    LogSerializer,
    ZoneConnectionSerializer,
    LogListSerializer,
    LogUpdateSerializer,
)
from .models import Zone, Log, ZoneConnection
from survivors.models import Survivor
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema  # type: ignore


class LogCreate(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(security=[{"Token": []}])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


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
