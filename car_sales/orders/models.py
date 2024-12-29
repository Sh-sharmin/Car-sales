from django.db import models
from django.contrib.auth.models import User
from car.models import Car

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.car.title}"
