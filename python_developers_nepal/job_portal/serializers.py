from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Company, HirePost, InternPost, JobPost


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # fields = ['id', 'company_name',
        #           'profile_description', 'company_website',
        #           'company_logo']
        fields = '__all__'


class InternPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InternPost
        fields = '__all__'


class JobPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
