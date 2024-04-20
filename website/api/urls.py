from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from website.api import views

router = routers.DefaultRouter()
router.register('certs', views.CertViewSet)
router.register('exps', views.EXPViewSet)
router.register('projects', views.ProjectViewSet)
router.register('skills', views.SkillViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version="v1",
        description="API for the portfolio Website"
    ),
    public=True
)

urlpatterns = [
    path('users/<str:username>', views.UserDetail.as_view(), name="user-detail-api"),
    #path('data', views.get_static_data, name="get_data"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('', include(router.urls)), 
    path('auth/', include('rest_framework.urls'), name="rest_framework"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]