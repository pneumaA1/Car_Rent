from django.urls import path

from webapp.views import *

app_name = 'webapp'

urlpatterns =[
    path('', index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
]