from rest_framework import serializers
from website.models import CERT, EXP, Project, User, SKILL


class CertSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    granted_on = serializers.DateField(format="%d/%m/%Y")
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

    start_date = serializers.DateField(format="%d/%m/%Y")
    end_date = serializers.DateField(format="%d/%m/%Y")
    
    class Meta:
        model = EXP
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    created_at = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Project
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSerializer(serializers.ModelSerializer):
    certs = CertSerializer(many=True)
    exps = EXPSerializer(many=True)
    projects = serializers.SerializerMethodField('get_user_projects')
    skills = SkillSerializer(many=True)

    def get_user_projects(self, instance):
        projects = Project.objects.filter(user=instance).order_by('created_at').reverse()
        return ProjectSerializer(projects, many=True, context=self.context).data
    
    def get_user_certs(self, instance):
        certs = CERT.objects.filter(user=instance).order_by('granted_on').reverse()
        return CertSerializer(certs, many=True, context=self.context).data
    
    def get_user_exps(self, instance):
        exps = EXP.objects.filter(user=instance).order_by('end_date').reverse()
        return EXPSerializer(exps, many=True, context=self.context).data

    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'resume', 'image', 'about', 'phone', 'telegram', 'github', 'certs', 'projects', 'exps', 'skills']