from rest_framework import permissions, viewsets, response
from rest_framework.decorators import api_view
from website.models import EXP, Project, CERT
from website.api.serializers import EXPSerializer, ProjectSerializer, CertSerializer
from portfolio.settings import BASE_DIR

import json

class CertViewSet(viewsets.ModelViewSet):
    queryset = CERT.objects.all()
    serializer_class = CertSerializer


class EXPViewSet(viewsets.ModelViewSet):
    queryset = EXP.objects.all()
    serializer_class = EXPSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@api_view(['GET', 'Post'])
def get_static_data(request):
    with open(BASE_DIR / 'statics/data.json', 'r+') as f:
        if request.method == "GET":
            data = json.load(f)
            return(response.Response(data))
        else:
            try:
                json.dump(request.data, f)
            except:
                return response.Response("POST requests must be a valid json")
            return response.Response(request.data)