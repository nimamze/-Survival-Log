from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import (
    LogSerializer,
    ZoneConnectionSerializer,
    LogListSerializer,
    LogUpdateSerializer,
    ZoneConnectionListSerializer,
    PuzzleAnswer,
)
from .models import Log, ZoneConnection
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from rest_framework.response import Response
from random import randint
import time
from rest_framework import status


class LogCreate(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]
    number_count = 0

    def randomValidate(self, request):
        random_number = 2
        if random_number % 2 == 0:
            if self.__class__.number_count < 3:
                self.__class__.number_count += 1
                time.sleep(2)
                return True
            else:
                self.__class__.number_count = 0
                user = request.user
                user.need_puzzle = True
                user.save()
                return False
        else:
            self.__class__.number_count = 0
            return True

    @swagger_auto_schema(security=[{"Token": []}])
    def post(self, request, *args, **kwargs):
        print(request.user.need_puzzle)
        if request.user.need_puzzle:
            return super().post(request, *args, **kwargs)
        if self.randomValidate(request):
            return super().post(request, *args, **kwargs)
        return redirect("puzzle")


class Puzzle(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"puzzle": "What is 2 + 2?"})

    def post(self, request):
        serializer = PuzzleAnswer(data=request.data)
        if serializer.is_valid():
            answer = str(serializer.validated_data.get("answer")).strip()  # type: ignore
            if answer == "4":
                user = request.user
                user.need_puzzle = False
                user.save()
                return Response(
                    {"message": "redirect to page log create"},
                    status=status.HTTP_301_MOVED_PERMANENTLY,
                )
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogList(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogListSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


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
