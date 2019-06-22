from django.shortcuts import render
from rest_framework import mixins, permissions, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoritesViewSets(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

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
        owner = self.request.query_params.get('owner_id')
        if owner:
            return queryset.filter(owner=owner)
        return queryset.none()
