from rest_framework import serializers
from . import models

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Zone
        fields = '__all__'
        

class LogSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = models.Log
        exclude = ['date','survivor']
      
        

class LogSerializerLIst(serializers.ModelSerializer):
    
    class Meta:

        model = models.Log
        exclude = ['date',]
class ZoneConnectionSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.ZoneConnection
        exclude = ['date']
        
class PuzzleSerializer(serializers.ModelSerializer):
    question = serializers.CharField(read_only=True)
    answer = serializers.CharField(write_only=True)
    class Meta:
        model = models.Puzzle

        fields = ['question','answer']


