from django.test import TestCase
from crudoperations_app import models

class ParentModelTestCase(TestCase):

    def setUp(self):
        self.parent_data = models.ParentData.objects.create(
            fathersname="Mohammad Y",
            mothersname="Miss X",
            street="42 43 Siddeswari",
            city="Dhaka",
            zipcode="1217")

    def test_parent_data(self):
        self.assertEqual(self.parent_data.fathersname, "Mohammad Y")
        self.assertEqual(self.parent_data.mothersname, "Miss X")
        self.assertEqual(self.parent_data.street, "42 43 Siddeswari")
        self.assertEqual(self.parent_data.city, "Dhaka")
        self.assertEqual(self.parent_data.zipcode, "1217")


class ChildModelTestCase(TestCase):

    def setUp(self):
        self.parent_data = models.ParentData.objects.create(
            fathersname="Mohammad Y",
            mothersname="Miss X",
            street="42 43 Siddeswari",
            city="Dhaka",
            zipcode="1217")

        self.child_data = models.ChildData.objects.create(
            childname="Mohammad YY", schoolname="XYZ school", relation=self.parent_data)

    def test_child_data(self):
        self.assertEqual(self.child_data.childname, "Mohammad YY")
        self.assertEqual(self.child_data.schoolname, "XYZ school")
        self.assertEqual(self.child_data.relation.fathersname, "Mohammad Y")
