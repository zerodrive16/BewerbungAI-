from rest_framework import serializers
from .models import Data, UserProfile


# Serializing the Data (Database format to JSON format)
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'