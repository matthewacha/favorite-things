from django.contrib.auth.models import User
from favorite_things.models import Favorites
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = ('url', 'name', 'description', 'ranking', 'Metadata',
                  'category', 'created_at', 'modified_date', 'audit_log')

