from rest_framework import serializers
from website.models import CERT, EXP, Project, User, SKILL


class CertSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = CERT
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = SKILL
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
    exps = EXPSerializer(many=True)
    projects = ProjectSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'resume', 'image', 'about', 'phone', 'telegram', 'github', 'certs', 'projects', 'exps', 'skills']