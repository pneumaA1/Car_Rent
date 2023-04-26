"""
Module containing a serializer for the Car model in the webapp application.
The CarSerializer class is a ModelSerializer provided by the Django Rest Framework.
 It is used to convert instances of the Car model into a JSON format suitable for use in API responses.
Usage:
To use this serializer, simply import it into your views or viewsets and pass an instance of the Car model to its serialize method.
"""
from rest_framework import serializers

from webapp.models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Serializes a Car model instance into JSON-compatible data.
    This serializer includes all fields defined on the Car model.
    """
    class Meta:
        model = Car
        fields = '__all__'
