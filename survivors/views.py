from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import SurvivorSerializer, SurvivorLoginSerializer
from .models import Survivor
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema  # type: ignore


class SurvivorSignUp(generics.CreateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer
    permission_classes = [permissions.AllowAny]


class SurvivorLogIn(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SurvivorLoginSerializer

    @swagger_auto_schema(
        operation_description="Login a user and return token",
        request_body=SurvivorLoginSerializer,
    )
    def post(self, request):
        serializer = SurvivorLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]  # type: ignore
            password = serializer.validated_data["password"]  # type: ignore
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
