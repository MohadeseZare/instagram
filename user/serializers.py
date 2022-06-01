# from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# from jwt import exceptions
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'mobile']

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs


