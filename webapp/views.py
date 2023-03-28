from django.shortcuts import render

from webapp.models import Car
def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def cars(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, 'webapp/cars.html', context=context)

def services(request):
    return render(request, 'webapp/services.html')

def contact(request):
    return render(request, 'webapp/contact.html')