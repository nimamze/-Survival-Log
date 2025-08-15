from rest_framework import serializers
from .models import Survivor
from django.contrib.auth import get_user_model
User = get_user_model()
class SurvivorSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = Survivor
        fields = ['username','password','email','is_verified']


    def create(self, validated_data):
        user = User(username=validated_data['username'],email=validated_data.get('email'))
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class survivorLoginSerializer(serializers.Serializer):
   
    username = serializers.CharField()
    password = serializers.IntegerField()




    
