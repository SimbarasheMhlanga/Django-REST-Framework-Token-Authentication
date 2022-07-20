"""datastore_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger import renderers


urlpatterns = [

    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='docs.html',
    #     extra_context={'schema_url': 'api_schema'}
    # ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('user/', include('crudoperations_app.api.urls')),
    path('account/', include('user_app.api.urls')),
    path('docs/', include_docs_urls(title='DataStoreAPI')),
    path('schema/', get_schema_view(
        title='DataStoreAPI', description='Guide for the CRUD operations',
        version="1.0.0"), name='openapi_schema'),
]
