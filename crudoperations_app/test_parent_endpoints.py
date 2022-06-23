from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from crudoperations_app import models


class ParentAPITestCases(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="Password@123")
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.parent_data = models.ParentData.objects.create(
            fathersname="Mohammad Y",
            mothersname=" Miss X",
            street="42 43 Siddeswari",
            city="Dhaka",
            zipcode="1217")

    def test_parent_get(self):

        get_response = self.client.get(reverse('parent-list'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_parent_create(self):
        data = {
            "fathersname": "Mohammad Y",
            "mothersname": " Miss X",
            "street": "42 43 Siddeswari",
            "city": "Dhaka",
            "zipcode": "1217"
        }

        get_response = self.client.post(reverse('parent-list'), data)
        self.assertEqual(get_response.status_code, status.HTTP_201_CREATED)

    def test_parent_get_individual(self):

        get_response = self.client.get(
            reverse(
                'parent-detail',
                args=(
                    self.parent_data.id,
                )))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data['fathersname'], "Mohammad Y")

    def test_parent_delete_individual(self):

        get_response = self.client.delete(
            reverse('parent-detail', args=(self.parent_data.id,)))
        self.assertEqual(get_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_parent_patch_individual(self):
        data = {
            "fathersname": "Mohammad Y",
            "mothersname": " Miss XXX"
        }
        get_response = self.client.patch(
            reverse(
                'parent-detail',
                args=(
                    self.parent_data.id,
                )),
            data)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_parent_put_individual(self):
        data = {
            "fathersname": "Mohammad YYYY",
            "mothersname": " Miss XXXX",
            "street": "42-43 Siddeswari",
            "city": "Dhaka",
            "zipcode": "1218"
        }
        get_response = self.client.put(
            reverse(
                'parent-detail',
                args=(
                    self.parent_data.id,
                )),
            data)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
