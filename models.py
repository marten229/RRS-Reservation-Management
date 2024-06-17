from django.db import models
from RestaurantManagement.models import Restaurant
from UserManagement.models import User
from MarketingFunctions.models import SpecialOffer
from RestaurantManagement.models import MenuItem
from django.utils import timezone
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
    rabattcode = models.ForeignKey(SpecialOffer, on_delete=models.SET_NULL, null=True, blank=True)
    gerichte = models.ManyToManyField(MenuItem, blank=True)
    buchungsdatum = models.DateField(default=timezone.now().date())
    buchungsuhrzeit = models.TimeField(default=timezone.now().time())

    def __str__(self):
        return f"{self.name} - {self.datum} at {self.uhrzeit}"