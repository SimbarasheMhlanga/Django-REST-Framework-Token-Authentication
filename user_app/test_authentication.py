from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_same_name", password="Password@123")

    def test_registration_regular_registration(self):
        data = {
            "username": "testcase1",
            "email": "test1@example.com",
            "password": "Password@123",
            "password2": "Password@123"

        }
        get_response = self.client.post(reverse('register'), data)
        self.assertEqual(get_response.status_code, status.HTTP_201_CREATED)

    def test_registration_short_password(self):
        data_password_check = {
            "username": "testcase2",
            "email": "test2@example.com",
            "password": "Pas",
            "password2": "Pas"

        }
        get_response = self.client.post(
            reverse('register'), data_password_check)
        self.assertEqual(get_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_password_mismatch(self):
        data_password_check = {
            "username": "testcase2",
            "email": "test2@example.com",
            "password": "Pass1",
            "password2": "Pass"

        }
        get_response = self.client.post(
            reverse('register'), data_password_check)
        self.assertEqual(get_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_same_name(self):
        data_same_name_check = {
            "username": "test_same_name",
            "email": "test3@example.com",
            "password": "Password@123",
            "password2": "Password@123"

        }
        get_response = self.client.post(
            reverse('register'), data_same_name_check)
        self.assertEqual(get_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_wrong_email(self):

        data_email_check = {
            "username": "testcase4",
            "email": "test4@",
            "password": "Password@123",
            "password2": "Password@123"

        }

        get_response = self.client.post(reverse('register'), data_email_check)
        self.assertEqual(get_response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="Password@123")

    def test_login(self):
        data = {
            "username": "example",
            "password": "Password@123"
        }
        get_response = self.client.post(reverse('login'), data)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)


class LogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="Password@123")

    def test_logout(self):
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        get_response = self.client.get(reverse('logout'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
