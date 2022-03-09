from rest_framework import serializers
from .models import *

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = number
        fields = ['number']