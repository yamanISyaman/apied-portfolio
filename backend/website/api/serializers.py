from rest_framework import serializers
from website.models import CERT, EXP, Project, User


class CertSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = CERT
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EXPSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = EXP
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = Project
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSerializer(serializers.ModelSerializer):
    certs = CertSerializer(many=True)
    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'certs']