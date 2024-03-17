from rest_framework import serializers
from website.models import CERT, EXP, Project, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CertSerializer(serializers.ModelSerializer):
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