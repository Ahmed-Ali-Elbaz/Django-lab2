from django.db import models
from django.shortcuts import reverse 

# Create your models here.

class Car(models.Model):
    car_model = models.CharField(max_length=200)
    car_price = models.IntegerField(default=0)
    production_year = models.DateField()    
    
    
    def __str__(self):
        return f"{self.car_model}"
    
    @classmethod
    def get_all_cars(cls):
        return cls.objects.all()
        
    
    def get_show_url(self):
        return reverse("cars.show", args=[self.id])
    
    def get_edit_url(self):
        return reverse("cars.edit", args=[self.id]) 

    def get_delete_url(self):
        return reverse("cars.delete", args=[self.id])