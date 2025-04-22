from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializer import CreateUserSerializer, UserSerialzier


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerialzier
  permission_classes = [IsAuthenticated]

  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def create(self, request, *args, **kwargs):
    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():
      user = serializer.save()

      user.set_password(serializer.validated_data['password'])
      user.save()

      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
