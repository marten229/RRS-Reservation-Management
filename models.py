from django.db import models
from RestaurantManagement.models import Restaurant
from UserManagement.models import User
# Create your models here.
####
####

class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefon_nummer = models.CharField(max_length=15)
    datum = models.DateField()
    uhrzeit = models.TimeField()
    dauer = models.IntegerField()
    anzahl_an_gästen = models.PositiveIntegerField()
    anmerkungen = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.datum} at {self.uhrzeit}"