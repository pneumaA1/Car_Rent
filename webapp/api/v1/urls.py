"""
Defines API endpoints for the 'car' resource.
Supported actions:
- GET /car/ - Retrieve a list of all cars
- POST /car/ - Create a new car
- GET /car/{id}/ - Retrieve details for a specific car
- PUT /car/{id}/ - Update a specific car
- DELETE /car/{id}/ - Delete a specific car
Usage:
1. Include this URL configuration in your project's urls.py file.
2. Make HTTP requests to the defined endpoints.
Example usage:
GET http://localhost:8000/car/ - retrieves a list of all cars
POST http://localhost:8000/car/ - creates a new car
GET http://localhost:8000/car/1/ - retrieves details for car with ID 1
PUT http://localhost:8000/car/1/ - updates car with ID 1
DELETE http://localhost:8000/car/1/ - deletes car with ID 1
"""
from django.urls import path, include
from rest_framework import routers
from webapp.api.v1.views import CarViewSet

router = routers.SimpleRouter()
router.register('car', CarViewSet, basename='car')

urlpatterns = [
    path('', include(router.urls)),

]
