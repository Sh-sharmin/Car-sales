from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from car.models import Car
from .models import Order

@login_required
def buy_now(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.quantity > 0:
        Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
    return redirect('profile')  
