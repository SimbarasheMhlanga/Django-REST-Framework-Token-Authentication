from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import RegisterAPIView, LogoutAPIView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/', LogoutAPIView.as_view(), name='logout')

]
