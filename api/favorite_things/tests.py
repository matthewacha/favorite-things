from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Favorites
from ..serializers import FavoriteSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_favorite(title='', ranking=0, category=''):
        if title != '' and ranking != 0:
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        favorites = [
            {
                title: 'biking',
                ranking: 2,
                category: 'outdoors'
            },
            {
                title: 'reading',
                ranking: 3,
                category: 'indoors'
            },
            {
                title: 'sky diving',
                ranking: 1,
                category: 'outdoors'
            }
        ]
        for fav in favorites:
            self.create_favorite(fav.title, fav.ranking, fav.category)


class GetFavoriteThings(BaseViewTest):

    def test_get_all_favorite_things(self):
        """
        This tests that all songs were created
        """
        response = self.client().get(reverse("all_favorites"))

        expected = Favorites.objects.all()
        serialized = FavoriteSerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)
