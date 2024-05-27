from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telefon_nummer = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()
    öffnungszeiten = models.CharField(max_length=100)
    beschreibung = models.TextField()
    image = models.ImageField(upload_to='restaurant_images', blank=True)

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefon_nummer = models.CharField(max_length=15)
    datum = models.DateField()
    uhrzeit = models.TimeField()
    anzahl_an_gästen = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.datum} at {self.uhrzeit}"