from rest_framework import serializers
from .models import Survivor

class SurvivorSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,style={'input_type': 'password'})

    class Meta:

        model = Survivor
        fields = ['username','password','email']

    def create(self,validated_data):
        user = Survivor.objects.create_user(
            username = validated_data['username'],
            email= validated_data['email'],
            password=validated_data['password']
        )
        return user