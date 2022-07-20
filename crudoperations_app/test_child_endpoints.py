from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from crudoperations_app import models

class ChildAPITestCases(APITestCase):

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
        self.child_data = models.ChildData.objects.create(
            childname="Mohammad YY", schoolname=" XYZ school", relation=self.parent_data)

    def test_child_create(self):
        data = {
            "childname": "Morich",
            "schoolname": "AbeeZee",
            "relation": self.parent_data
        }
        get_response = self.client.post(
            reverse(
                'child-create',
                args=(
                    self.parent_data.id,
                )),
            data)
        self.assertEqual(get_response.status_code, status.HTTP_201_CREATED)

    def test_child_get(self):

        get_response = self.client.get(reverse('child-list'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_child_get_individual(self):

        get_response = self.client.get(
            reverse(
                'child-detail',
                args=(
                    self.child_data.id,
                )))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_child_delete_individual(self):

        get_response = self.client.delete(
            reverse('child-detail', args=(self.child_data.id,)))
        self.assertEqual(get_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_child_patch_individual(self):
        data = {
            "childname": "Mohammad YY",
            "schoolname": "XX YY XX School Changed"
        }
        get_response = self.client.patch(
            reverse(
                'child-detail',
                args=(
                    self.child_data.id,
                )),
            data)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_child_put_individual(self):
        data = {
            "childname": "Mohammad Changed",
            "schoolname": "X School Changed"
        }
        get_response = self.client.put(
            reverse(
                'child-detail',
                args=(
                    self.child_data.id,
                )),
            data)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
