from django.shortcuts import render
# Create your views here.
from cars.models import Car
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from cars.forms import CarModelForm

def CarIndex(request):
    allcars = Car.get_all_cars()    
    return render(request, "cars/index.html", context={"cars":allcars})   

class CarDetails(DetailView):
    model = Car
    template_name = "cars/show.html"
    

class CreateCarView(CreateView):
    template_name = "cars/create.html"
    form_class = CarModelForm
    success_url = "/cars/index"
    
class EditCarView(UpdateView):
    
    template_name = "cars/edit.html"
    form_class = CarModelForm
    success_url = "/cars/index"
    model = Car
    
    
class DeleteCarView(DeleteView):
    
    template_name = "cars/delete.html"
    success_url = "/cars/index"
    model = Car