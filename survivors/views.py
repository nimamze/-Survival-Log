from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import SurvivorSerializer
from .models import Survivor
from rest_framework import status

class SurvivorSignUp(generics.CreateAPIView):

    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer
    permission_classes = [permissions.AllowAny]

class SurvivorLogIn(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username,password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Informations'}, status=status.HTTP_401_UNAUTHORIZED)