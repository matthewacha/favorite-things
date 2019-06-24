from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Favorite
from .serializers import FavoriteSerializer


class BaseViewTest(APITestCase, APIClient):
    client = APIClient()

    @staticmethod
    def create_favorite(user, title='', ranking=0, category=''):
        Favorite.objects.create(owner=user, title=title,
                                metadata="\"{}\"", ranking=ranking,
                                category=category, description="helping hand")

    def setUp(self):
        favorites = [
            {
                'title': 'biking',
                'ranking': 2,
                'category': 'pe'
            },
            {
                'title': 'reading',
                'ranking': 3,
                'category': 'pl'
            },
            {
                'title': 'sky diving',
                'ranking': 1,
                'category': 'pe'
            }
        ]

        user = User.objects.create_user(username='tesubd0lo0dj30e',
                                        password='password')
        user.firstname = 'james'
        user.save()

        for fav in favorites:
            self.create_favorite(user, fav['title'], fav['ranking'],
                                 fav['category'])

    def tearDown(self):
        user = User.objects.get(username='tesubd0lo0dj30e')
        favorites = Favorite.objects.filter(owner=user.id)
        for fav in favorites:
            fav.delete()


class GetFavoriteThings(BaseViewTest):

    def test_get_all_favorite_things(self):
        """
        This tests that all favorites were created
        """

        user1 = User.objects.create_user(username='tesubd0lo0e',
                                         password='password')
        self.create_favorite(user1, 'title', 10, 'people')

        user = User.objects.get(username='tesubd0lo0dj30e')

        url = '/v1/favorite/?owner_id={}'.format(user.id)
        response = APIClient().get(url)

        expected = Favorite.objects.filter(owner=user)
        serialized = FavoriteSerializer(expected, many=True)

        self.assertEqual(len(response.data), len(serialized.data))

    def test_get_one_favorite_thing(self):
        """
        This tests that one favorite thing is returned
        """
        user = User.objects.get(username='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(owner=user.id).first()
        url = '/v1/favorite/{}/?owner_id={}'.format(favorite.id, user.id)
        response = APIClient().get(url)

        expected = Favorite.objects.get(pk=favorite.id)
        serialized = FavoriteSerializer(expected, many=False)

        self.assertEqual(response.data['favorite'], serialized.data)
        self.assertEqual(response.status_code, 200)


class PostFavoriteThings(BaseViewTest):

    def test_user_can_post_favorite(self):
        """
        This method tests that a registered user can post a favorite thing
        """

        user = User.objects.get(username='tesubd0lo0dj30e')
        url = '/v1/favorite/'

        favorite_thing = {
            "owner": user.id,
            "title": "main test is here",
            "description": "helping hand",
            "ranking": 7,
            "category": "pe",
            "metadata": "\"{}\""
        }

        response = APIClient().post(url, favorite_thing)
        self.assertEqual(response.status_code, 201)


class UpdateFavoriteThings(BaseViewTest):

    def test_update_favorite_thing(self):
        """
        This tests that a user only update their favorite things
        """
        user = User.objects.get(username='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(owner=user.id).first()
        get_url = '/v1/favorite/{}/?owner_id={}'.format(favorite.id, user.id)

        favorite_update = {'owner': 5,
                           'title': 'mountain biking',
                           'description': 'helping hand',
                           'ranking': 2, 'category': 'pe',
                           'metadata': '"\\"{}\\""'}
        update_response = APIClient().put(get_url, favorite_update)

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.data['title'],
                         favorite_update['title'])
