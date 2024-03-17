from django.urls import include, path
from rest_framework import routers

from website.api import views

router = routers.DefaultRouter()
router.register('certs', views.CertViewSet)
router.register('exps', views.EXPViewSet)
router.register('projects', views.ProjectViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/<str:username>', views.UserDetail.as_view(), name="user-detail-api"),
    path('data', views.get_static_data, name="get_data"),
    path('auth/', include('rest_framework.urls'), name="rest_framework"),
]