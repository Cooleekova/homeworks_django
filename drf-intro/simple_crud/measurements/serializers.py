from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Measurement, Project


class MeasurementsSerializer(ModelSerializer):

    class Meta:
        model = Measurement
        fields = 'id', 'value'


class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = 'id', 'name'
