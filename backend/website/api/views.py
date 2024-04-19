from django.contrib.auth import logout
from rest_framework import permissions, viewsets, response, generics
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.shortcuts import redirect
from website.models import EXP, Project, CERT,  User, SKILL
from website.api.permissions import UserModifyOrReadOnly
from website.api.serializers import EXPSerializer, ProjectSerializer, CertSerializer, UserSerializer, SkillSerializer
from portfolio.settings import BASE_DIR

import json


class CertViewSet(viewsets.ModelViewSet):
    queryset = CERT.objects.all()
    serializer_class = CertSerializer
    permission_classes = [UserModifyOrReadOnly]


    # filtering on user
    def get_queryset(self):

        return self.queryset.filter(user=self.request.user).order_by('granted_on').reverse()


    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def retrieve(self, *args, **kwargs):
        return super(CertViewSet, self).retrieve(*args, **kwargs)
    

    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, *args, **kwargs):
        return super(CertViewSet, self).list(*args, **kwargs)
    

class SkillViewSet(viewsets.ModelViewSet):
    queryset = SKILL.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [UserModifyOrReadOnly]


    # filtering on user
    def get_queryset(self):

        return self.queryset.filter(user=self.request.user).order('order')


    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def retrieve(self, *args, **kwargs):
        return super(SkillViewSet, self).retrieve(*args, **kwargs)
    

    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, *args, **kwargs):
        return super(SkillViewSet, self).list(*args, **kwargs)


class EXPViewSet(viewsets.ModelViewSet):
    queryset = EXP.objects.all()
    serializer_class = EXPSerializer
    permission_classes = [UserModifyOrReadOnly]


    # filtering on user
    def get_queryset(self):

        return self.queryset.filter(user=self.request.user).order_by("end_date").reverse()


    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def retrieve(self, *args, **kwargs):
        return super(EXPViewSet, self).retrieve(*args, **kwargs)
    

    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, *args, **kwargs):
        return super(EXPViewSet, self).list(*args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [UserModifyOrReadOnly]


    # filtering on user
    def get_queryset(self):

        return self.queryset.filter(user=self.request.user).order_by("created_at").reverse()


    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def retrieve(self, *args, **kwargs):
        return super(ProjectViewSet, self).retrieve(*args, **kwargs)
    

    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, *args, **kwargs):
        return super(ProjectViewSet, self).list(*args, **kwargs)


class UserDetail(generics.RetrieveAPIView):
    
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserModifyOrReadOnly]

    @method_decorator(cache_page(600))
    def retrieve(self, *args, **kwargs):
        return super(UserDetail, self).retrieve(*args, **kwargs)
