from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from api.users.models import CustomUser
from api.users.serializers import CustomUserSerializer


class BaseViewTest(APITestCase, APIClient):
    client = APIClient()

    def setUp(self):
        pass


class PostUserTest(BaseViewTest):
    def test_newuser_login(self):
        """
        Tests that a new user logs the application
        """
        url = '/v1/user/'
        response = APIClient().post(url, {"name": "testuser1"})

        self.assertEqual(response.status_code, 201)

    def test_user_logsin_uniquely(self):
        """
        Tests whether who a user is uniquely created
        """
        url = '/v1/user/'
        APIClient().post(url, {"name": "testuser1"})
        response = APIClient().post(url, {"name": "testuser1"})

        self.assertEqual(response.status_code, 200)

