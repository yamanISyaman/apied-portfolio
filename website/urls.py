from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/v1/', include("website.api.urls"))
]