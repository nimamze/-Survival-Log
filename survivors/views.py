from rest_framework import generics, permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from .serializers import *
from logs.serializers import *
from logs.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated

    
class SurvivorSignUp(generics.CreateAPIView):
    serializer_class =SurvivorSerializer

class SurvivorLogIn(APIView):
    
    def post(self, request):
        serializers = survivorLoginSerializer(data = request.data)
        if serializers.is_valid():
            cd = serializers.validated_data
            user = authenticate(username=cd['username'], password=cd['password'])
        if user:
            login(request,user)
            
            return Response({'succsess': 'valid'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=401)


class SurvivorLog(generics.ListAPIView,):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    
    
class createloge(APIView):

        queryset = Log.objects.all()
        serializer_class = LogSerializer
        def post(self,request):
            serializers = LogSerializer(data = request.data)
            if serializers.is_valid():
                survivor = Log.objects.filter(survivor__username =request.user)
                serializers.create(survivor = survivor)
            return Response({'succsess': 'valid'}, status=status.HTTP_200_OK)
            
    

class createLog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)










