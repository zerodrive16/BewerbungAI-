from rest_framework import serializers
from .models import Data


# Serializing the Data (Database format to JSON format)
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'