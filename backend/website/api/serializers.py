from rest_framework import serializers
from website.models import CERT, EXP, Project, User


class CertSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="user-detail-api",
        lookup_field='username'
    )
    class Meta:
        model = CERT
        fields = "__all__"

class EXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EXP
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    certs = CertSerializer(many=True)
    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'certs']