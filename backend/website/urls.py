from django.contrib import admin
from django.urls import path, include
from website import views
from django.conf import settings
from django.conf.urls.static import static

import os



urlpatterns = [
    path('', views.index, name="index"),
    path('api/v1/', include("website.api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)