from django.urls import path
from .views import buy_now

urlpatterns = [
    path('buy/<int:car_id>/', buy_now, name='buy_now'),
]
