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
        

class ZoneConnectionSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.ZoneConnection
        exclude = ['date']

