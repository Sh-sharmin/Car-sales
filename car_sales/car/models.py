from django.contrib.auth.models import User
from django.db import models
from brand.models import Brand 

class Car(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='uploads/')
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Guest'} on {self.car.title}"
    

