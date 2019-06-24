from django.contrib.auth.models import User
from api.favorite_things.models import Favorite
from rest_framework import serializers
from rest_framework.response import Response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('owner', 'title', 'description', 'ranking', 'category',
                  'created_at', 'modified_at', 'owner', 'metadata', 'id')

    def validate_ranking(self, ranking):
        if isinstance(ranking, int) and ranking > 0:
            return ranking
        raise serializers.ValidationError(
                'Ranking should be an integer greater than 0'
            )

    # validate that the ranking, title is unique to a user
