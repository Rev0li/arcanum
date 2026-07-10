"""Routage racine. La page d'accueil et /healthz arrivent avec le ticket #32."""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
