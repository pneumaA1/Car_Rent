from django.urls import path

from webapp.api.v1.views import CarsAPIView

urlpatterns = [
    path('carslist/', CarsAPIView().as_view()),
]
