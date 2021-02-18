"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import (
    token_obtain_pair,
    token_refresh,
    token_verify
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

from .settings import SHOW_ADMIN, SHOW_DOCS

SchemaView = get_schema_view(
    openapi.Info(title="Response API", default_version='v1'),
    authentication_classes=(SessionAuthentication, ),
    public=True,
    permission_classes=(IsAdminUser, ),
)

urlpatterns = [
    path('token', token_obtain_pair, name='token-create'),
    path('token/refresh', token_refresh, name='token-refersh'),
    path('token/verify', token_verify, name='token-name')
]
if SHOW_ADMIN:
    urlpatterns.append(path('admin', admin.site.urls))

if SHOW_DOCS:
    urlpatterns.append(path('docs', SchemaView.with_ui(), name='docs'))
