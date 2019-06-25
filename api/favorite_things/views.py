from django.shortcuts import render
from rest_framework import mixins, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .models import Favorite
from .serializers import FavoriteSerializer
import coreapi
import coreschema
from rest_framework import schemas


class FavoritesViewSets(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    """
    retrieve:
    Return an existing favorite belonging to a user.

    destroy:
    Deletes an existing favorites belonging to the user

    create:
    Adds a new favorite

    update:
    Updates an existing favorite thing
    """
    permission_classes = [AllowAny]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    schema = schemas.AutoSchema(
        manual_fields=[
            coreapi.Field("customuser_id",
                          required=True,
                          location="query",
                          schema=coreschema.Integer()),
        ]
    )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except (Exception):
            response = {
                        'message': 'The resource does not exist',
                        'status': 404,
                        'success': False
                        }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        self.perform_destroy(instance)
        response = {
                    'message': '{} has been deleted'.format(instance.title),
                    'status': 200,
                    'success': True
                    }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except (Exception):
            response = {
                        'message': 'The resource does not exist',
                        'status': 404,
                        'success': False
                        }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        response = {
                    'favorite': serializer.data,
                    'status': 200,
                    'success': True
                    }
        return Response(response, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super(FavoritesViewSets, self).get_queryset()
        customuser = self.request.query_params.get('customuser_id')
        if customuser:
            return queryset.filter(customuser=customuser)
        return queryset.none()

    def create(self, request, *args, **kwargs):
        queryset = super(FavoritesViewSets, self).get_queryset()
        favorite_title = request.data.get('title')
        customuser = request.data.get('customuser')
        favorite_thing = queryset.filter(customuser=customuser,
                                         title=favorite_title)
        if not favorite_thing:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)
        response = {
            'message': 'A favorite item with that title already exists',
            'status': 409,
            'success': False
            }
        return Response(response, status=status.HTTP_409_CONFLICT)
