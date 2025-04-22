from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']


class CreateUserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password']
