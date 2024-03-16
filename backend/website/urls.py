from django.contrib import admin
from django.urls import path, include, re_path
from website import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

import os

schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version="v1",
        description="API for the portfolio Website"
    ),
    public=True
)

urlpatterns = [
    path('', views.index, name="index"),
    path('api/v1/', include("website.api.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]