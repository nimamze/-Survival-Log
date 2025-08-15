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
from random import randrange
from time import sleep
from django.shortcuts import redirect

    
class SurvivorSignUp(generics.CreateAPIView):
    serializer_class =SurvivorSerializer

class SurvivorLogIn(APIView):
    serializer_class = survivorLoginSerializer
    def post(self, request):
        serializers = survivorLoginSerializer(data = request.data)
        if serializers.is_valid():
            cd = serializers.validated_data
            user = authenticate(username=cd['username'], password=cd['password'])
        if user:
            login(request,user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'success': 'valid', 'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=401)


class SurvivorLog(generics.ListAPIView,):
    queryset = Log.objects.all()
    serializer_class = LogSerializerLIst
    
    
class createlog(APIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    
   
    def post(self, request):
        serializer = LogSerializer(data=request.data)
        even_numbers= Survivor.objects.get(pk = request.user.pk)
        if serializer.is_valid():


            
            number = randrange(2,100,2)
            if number % 2 == 0:
               
                even_numbers.consecutive_even_numbers +=1

                sleep(2)
                even_numbers.save()
            else:
                even_numbers.consecutive_even_numbers = 0
                even_numbers.save()
            if even_numbers.consecutive_even_numbers >= 3:
                return redirect('puzzle')
            serializer.save(survivor=request.user)
            return Response({'success': 'log created'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    

class createLog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    def get_queryset(self):
        
        return Log.objects.filter(survivor = self.request.user,survivor__is_verified = True).select_related('survivor','zone')
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)



class PuzzleView(generics.ListCreateAPIView):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        serializer = PuzzleSerializer(data=request.data)
        if serializer.is_valid():
            answer = serializer.validated_data['answer']
            if answer == '10':
                return redirect('createlog')
            return Response({'error': 'wrong answer'})
