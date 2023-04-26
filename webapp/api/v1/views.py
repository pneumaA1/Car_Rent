from rest_framework import viewsets
from webapp.api.v1.serializers import CarSerializer
from webapp.models import Car


class CarViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD operations for the Car model.
     Attributes:
    queryset (QuerySet): A QuerySet containing all instances of the Car model.
    serializer_class (Serializer): The serializer class used to serialize and deserialize Car instances.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
