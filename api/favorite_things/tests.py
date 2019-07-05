from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Favorite
from api.users.models import CustomUser
from api.favorite_things.serializers import FavoriteSerializer


class BaseViewTest(APITestCase, APIClient):
    client = APIClient()

    @staticmethod
    def create_favorite(user, title='', ranking=0, category=''):
        Favorite.objects.create(customuser=user, title=title,
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

        user = CustomUser.objects.create(name='tesubd0lo0dj30e')
        user.save()
        for fav in favorites:
            self.create_favorite(user, fav['title'], fav['ranking'],
                                 fav['category'])

    def tearDown(self):
        user = CustomUser.objects.get(name='tesubd0lo0dj30e')
        favorites = Favorite.objects.filter(customuser=user.id)
        for fav in favorites:
            fav.delete()


class GetFavoriteThings(BaseViewTest):

    def test_get_all_favorite_things(self):
        """
        This tests that all favorites were created
        """

        user1 = CustomUser.objects.create(name='tesubd0lo0e')
        user1.save()
        self.create_favorite(user1, 'title', 10, 'people')

        user = CustomUser.objects.get(name='tesubd0lo0dj30e')

        url = '/v1/favorite/?customuser_id={}'.format(user.id)
        response = APIClient().get(url)

        expected = Favorite.objects.filter(customuser=user)
        serialized = FavoriteSerializer(expected, many=True)

        self.assertEqual(len(response.data), len(serialized.data))

    def test_get_one_favorite_thing(self):
        """
        This tests that one favorite thing is returned
        """
        user = CustomUser.objects.get(name='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(customuser=user.id).first()
        url = '/v1/favorite/{}/?customuser_id={}'.format(favorite.id, user.id)
        response = APIClient().get(url)

        expected = Favorite.objects.get(pk=favorite.id)
        serialized = FavoriteSerializer(expected, many=False)

        self.assertEqual(response.data['favorite'], serialized.data)
        self.assertEqual(response.status_code, 200)

    def test_get_throws_exception(self):
        """
        This tests that a user cannot get a
        favorite thing that does not exist
        """
        user = CustomUser.objects.get(name='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(customuser=user.id).first()
        url = '/v1/favorite/{}/?customuser_id={}'.format(109, user.id)
        response = APIClient().get(url)

        expected = Favorite.objects.get(pk=favorite.id)
        serialized = FavoriteSerializer(expected, many=False)
        message = response.data['message']
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, 'The resource does not exist')


class PostFavoriteThings(BaseViewTest):

    def test_user_can_post_favorite(self):
        """
        This method tests that a registered user can post a favorite thing
        """

        user = CustomUser.objects.get(name='tesubd0lo0dj30e')
        url = '/v1/favorite/'

        favorite_thing = {
            "customuser": user.id,
            "title": "main test is here",
            "description": "helping hand",
            "ranking": 7,
            "category": "pe",
            "metadata": "\"{}\""
        }

        response = APIClient().post(url, favorite_thing)
        self.assertEqual(response.status_code, 201)

    def test_user_can_post_unique_favorite(self):
        """
        This method tests that a registered user can post a unique
        favorite thing
        """

        user = CustomUser.objects.get(name='tesubd0lo0dj30e')
        url = '/v1/favorite/'

        favorite_thing = {
            "customuser": user.id,
            "title": "main test is here",
            "description": "helping hand",
            "ranking": 7,
            "category": "pe",
            "metadata": "\"{}\""
        }
        APIClient().post(url, favorite_thing)
        response = APIClient().post(url, favorite_thing)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['message'],
                         'A favorite item with that title already exists')


class UpdateFavoriteThings(BaseViewTest):

    def test_update_favorite_thing(self):
        """
        This tests that a user only update their favorite things
        """
        user = CustomUser.objects.get(name='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(customuser=user.id).first()
        update_url = '/v1/favorite/{}/?customuser_id={}'.format(
            favorite.id, user.id)

        favorite_update = {'customuser': user.id,
                           'title': 'mountain biking',
                           'description': 'helping hand',
                           'ranking': 2, 'category': 'pe',
                           'metadata': '"\\"{}\\""'}
        update_response = APIClient().put(update_url, favorite_update)

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.data['title'],
                         favorite_update['title'])


class DeleteFavoriteThings(BaseViewTest):

    def test_delete_favorite_thing(self):
        """
        This tests that a user only deletes their favorite things
        """
        user = CustomUser.objects.get(name='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(customuser=user.id).first()
        delete_url = '/v1/favorite/{}/?customuser_id={}'.format(
            favorite.id, user.id)

        delete_response = APIClient().delete(delete_url)

        self.assertEqual(delete_response.status_code, 200)

    def test_delete_favorite_exception(self):
        """
        This tests that an exception is throen when trie to delete a favorite
        thing that does not exist
        """
        user = CustomUser.objects.get(name='tesubd0lo0dj30e')

        favorite = Favorite.objects.filter(customuser=user.id).first()
        delete_url = '/v1/favorite/{}/?customuser_id={}'.format(
            102, user.id)

        delete_response = APIClient().delete(delete_url)

        self.assertEqual(delete_response.status_code, 404)
        self.assertEqual(delete_response.data['message'], 'The resource does not exist')

