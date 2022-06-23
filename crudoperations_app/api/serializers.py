'''This module serializes parent and child data'''
from rest_framework import serializers
from crudoperations_app.models import ParentData, ChildData


class ChildDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChildData
        fields = ['id', 'childname', 'schoolname']


class ParentDataSerializer(serializers.ModelSerializer):

    child = ChildDataSerializer(many=True, read_only=True)

    class Meta:
        model = ParentData
        fields = "__all__"
