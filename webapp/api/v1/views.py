from rest_framework import generics

from webapp.api.v1.serializers import CarSerializer
from webapp.models import Car


class CarsAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
