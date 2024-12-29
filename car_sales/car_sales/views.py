from django.shortcuts import render
from brand.models import Brand
from car.models import Car
def home(request):
    brands = Brand.objects.all() 
    brand_filter = request.GET.get('brand')
    if brand_filter:
        cars = Car.objects.filter(brand__name=brand_filter)  
    else:
        cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands})