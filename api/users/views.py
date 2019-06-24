from django.shortcuts import render
from rest_framework import mixins, permissions, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSets(mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        instance = CustomUser.objects.filter(
            name=self.request.data['name']).first()
        if not instance:
            try:
                user = CustomUser.objects.create(
                    name=self.request.data['name'])
                user.save()
            except Exception:
                raise Exception('An error occured while creating the users')
            return Response({"user": {"name": user.name, "id": user.id},
                             "success": True}, status=status.HTTP_201_CREATED)
        return Response({"message": "user exists",
                         "success": True,
                         "user": {"name": instance.name, "id": instance.id}},
                        status=status.HTTP_200_OK)
