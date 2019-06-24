from .models import CustomUser
from rest_framework import serializers
from rest_framework.response import Response


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'id')
