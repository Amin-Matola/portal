from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r"restraunts/?", include("apps.restraunts.urls")),
    path("", include("apps.sample.urls")),             # UI Kits Html files
]
