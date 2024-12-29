from django.urls import path
from .views import CarDetailView

urlpatterns = [
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_details'),  # Dynamic URL for car details
]
