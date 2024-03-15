from rest_framework import permissions, viewsets

from website.models import EXP, Project, CERT
from website.api.serializers import EXPSerializer, ProjectSerializer, CertSerializer

class CertViewSet(viewsets.ModelViewSet):
    queryset = CERT.objects.all()
    serializer_class = CertSerializer


class EXPViewSet(viewsets.ModelViewSet):
    queryset = EXP.objects.all()
    serializer_class = EXPSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer