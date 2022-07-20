from django.db import models

class ParentData(models.Model):
    fathersname = models.CharField(max_length=30)
    mothersname = models.CharField(max_length=30)
    street = models.CharField(max_length=60)
    city = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return f"Parent's Name : {self.fathersname} and {self.mothersname}"


class ChildData(models.Model):

    childname = models.CharField(max_length=30)
    schoolname = models.CharField(max_length=100)
    relation = models.ForeignKey(
        ParentData,
        on_delete=models.CASCADE,
        related_name="child")

    def __str__(self):
        return self.childname
