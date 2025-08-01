from rest_framework import serializers
from . import models

class SurvivorSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = models.Survivor
        fields = ['username','password','email']