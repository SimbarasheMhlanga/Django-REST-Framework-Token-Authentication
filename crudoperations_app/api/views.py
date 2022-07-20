'''This module contains the DRF views for CRUD operations'''
from rest_framework import generics
from .serializers import ParentDataSerializer, ChildDataSerializer
from crudoperations_app.models import ParentData, ChildData
from datastore_app.mixins import AppAuthPermMixin

# ALL THE CLASSES INHERIT
# PREDEFINED AUTHENTICATION
# AND PERMISSION CLASSES VIA
# AppAuthPermMixin

class ParentListCreateAPIView(AppAuthPermMixin, generics.ListCreateAPIView):
    '''Lists collection of data, creates data'''
    queryset = ParentData.objects.all()
    serializer_class = ParentDataSerializer


class ParentRetrieveUpdateDestroyAPIView(
        AppAuthPermMixin,
        generics.RetrieveUpdateDestroyAPIView):
    '''Retrieves updates partial-updates and deletes individual parent data'''

    queryset = ParentData.objects.all()
    serializer_class = ParentDataSerializer
    lookup_field = 'pk'

class ChildRetrieveUpdateDestroyAPIView(
        AppAuthPermMixin,
        generics.RetrieveUpdateDestroyAPIView):
    '''Retrieves updates partial-updates and deletes individual child data'''
    queryset = ChildData.objects.all()
    serializer_class = ChildDataSerializer
    lookup_field = 'id'

class ChildListAPIView(AppAuthPermMixin, generics.ListAPIView):
    '''Lists collection of child data'''
    queryset = ChildData.objects.all()
    serializer_class = ChildDataSerializer


class ChildCreateAPIView(AppAuthPermMixin, generics.CreateAPIView):
    '''Creates individual child data under a unique parent'''
    queryset = ChildData.objects.all()
    serializer_class = ChildDataSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        parent = ParentData.objects.get(pk=pk)
        serializer.save(relation=parent)
