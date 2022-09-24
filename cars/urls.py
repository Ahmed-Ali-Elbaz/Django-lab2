from django.urls import path
from cars.views import CarIndex, CarDetails, CreateCarView, EditCarView, DeleteCarView
urlpatterns = [
    path('index',CarIndex ),
    path('<int:pk>',CarDetails.as_view(), name= 'cars.show'),
    path('create', CreateCarView.as_view()),
    path('edit/<int:pk>', EditCarView.as_view(), name= 'cars.edit'),
    path('delete/<int:pk>', DeleteCarView.as_view(), name= 'cars.delete')


]   