'''This module contains DRF views for log in and logout functionality'''
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from user_app.api.serializers import RegSerializer
from user_app import models

class LogoutAPIView(generics.GenericAPIView):
    '''Logs out user or deletes token'''
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        '''Deletes authentication token'''
        request.user.auth_token.delete()
        return Response({'success': 'Logged out successfully'},
                        status=status.HTTP_200_OK)


class RegisterAPIView(generics.GenericAPIView):
    '''Registers user'''
    serializer_class = RegSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            user_account = serializer.save()
            data['response'] = "Registration Successful!"
            token = Token.objects.get(user=user_account).key
            data['token'] = token

        return Response(data, status.HTTP_201_CREATED)
