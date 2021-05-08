from rest_framework.serializers import ModelSerializer
from .models import Measurement, Project


class MeasurementsSerializer(ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'value', 'project', 'created_at', 'updated_at']


class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at']
