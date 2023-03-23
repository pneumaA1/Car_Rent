from django.urls import path

from webapp.views import *

app_name = 'webapp'

urlpatterns =[
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cars/', cars, name='cars'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
]