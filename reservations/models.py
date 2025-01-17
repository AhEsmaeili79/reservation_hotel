from django.db import models
from house.models import House
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    arrive_date = models.DateField()
    exit_date = models.DateField()
    count_of_passengers = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=0)
