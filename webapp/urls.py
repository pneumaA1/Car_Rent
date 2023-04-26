"""
Defines the URL patterns for the webapp application.

Includes views for displaying the home page, about page, car list view,
car detail view, services view, contact view, user authentication views
(login, logout, registration), and registration success view.

URL patterns:
- '' (home): index view
- 'about/': AboutView (class-based) with name 'about'
- 'cars/': CarListView (class-based) with name 'cars'
- 'cars/<int:pk>': CarDetailView (class-based) with name 'car_detail'
- 'services/': ServicesView (class-based) with name 'services'
- 'contact/': ContactView (class-based) with name 'contact'
- 'accounts/login/': CRLoginView (class-based) with name 'login'
- 'accounts/logout/': CRLogoutView (class-based) with name 'logout'
- 'accounts/register/': RegisterUserView (class-based) with name 'register'
- 'accounts/regitster/done/': RegisterDoneView (class-based) with name 'register_done'
"""
from django.urls import path

from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('accounts/login/', CRLoginView.as_view(), name='login'),
    path('accounts/logout/', CRLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/regitster/done/', RegisterDoneView.as_view(),
         name='register_done'),
]
