from django.db import models

from account.models import Profile


class Taxi(models.Model):
    name = models.CharField(max_length=125)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    address = models.CharField(max_length=125)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class StatusType(models.Model):
    rating = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.rating} - {self.taxi.name}'

class StatusDriver(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=1)
    rating = models.IntegerField()

    class Meta:
        unique_together = ['profile', ]

    def __str__(self):
        return f'{self.taxi.id} -{self.rating}'