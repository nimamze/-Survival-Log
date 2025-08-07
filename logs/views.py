from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import ZoneSerializer, LogSerializer, ZoneConnectionSerializer
from .models import Zone, Log, ZoneConnection
from survivors.models import Survivor
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema  # type: ignore


class LogCreate(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(security=[{"Token": []}])
    def post(self, request):
        return super().post(self, request)
