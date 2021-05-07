from rest_framework.viewsets import ModelViewSet
from .models import Measurement, Project
from .serializers import MeasurementsSerializer, ProjectsSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
