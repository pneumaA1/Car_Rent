from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from webapp.models import Car


def index(request):
    cars = Car.objects.all()[:3]
    main_car = Car.objects.filter(is_main=True).first()
    context = {"cars": cars,
               "main_car": main_car}
    return render(request, 'webapp/index.html', context=context)


class AboutView(TemplateView):
    template_name = 'webapp/about.html'




class CarListView(ListView):
    template_name = 'webapp/cars.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 3)
        page_number = self.request.GET.get('page')
        page_objs = paginator.get_page(page_number)
        context = {"page_objs": page_objs}
        return super().get_context_data(**context)

    def get_queryset(self):
        return Car.objects.all()


class CarDetailView(DetailView):
    model = Car
    template_name = 'webapp/car_detail.html'


class ServicesView(TemplateView):
    template_name = 'webapp/services.html'


class ContactView(TemplateView):
    template_name = 'webapp/contact.html'
