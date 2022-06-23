from django.urls import path, include
from crudoperations_app.api.views import (
    ParentListCreateAPIView,
    ParentRetrieveUpdateDestroyAPIView,
    ChildCreateAPIView,
    ChildListAPIView,
    ChildRetrieveUpdateDestroyAPIView)


urlpatterns = [
    path(
        'parent/',
        ParentListCreateAPIView.as_view(),
        name='parent-list'),
    path(
        'parent/<int:pk>/',
        ParentRetrieveUpdateDestroyAPIView.as_view(),
        name='parent-detail'),
    
    path(
        'parent/<int:pk>/child/',
        ChildCreateAPIView.as_view(),
        name='child-create'),
    path(
        'child/',
        ChildListAPIView.as_view(),
        name='child-list'),
    path(
        'child/<int:id>/',
        ChildRetrieveUpdateDestroyAPIView.as_view(),
        name='child-detail'),
    
]
