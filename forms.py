from django import forms
from .models import Reservation
from RestaurantManagement.models import MenuItem
from MarketingFunctions.models import SpecialOffer

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'telefon_nummer', 'datum', 'uhrzeit', 'anzahl_an_gästen', 'dauer', 'anmerkungen', 'rabattcode', 'gerichte']

    def __init__(self, *args, **kwargs):
        restaurant = kwargs.pop('restaurant', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if restaurant:
            self.fields['gerichte'].queryset = MenuItem.objects.filter(restaurant=restaurant)
            self.fields['rabattcode'].queryset = SpecialOffer.objects.filter(restaurant=restaurant)
            self.fields['rabattcode'].label_from_instance = lambda obj: f"{obj.code} - {obj.description[:30]}"

class ReservationFormLoggedIn(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['datum', 'uhrzeit', 'anzahl_an_gästen', 'dauer', 'anmerkungen', 'rabattcode', 'gerichte']

    def __init__(self, *args, **kwargs):
        restaurant = kwargs.pop('restaurant', None)
        super(ReservationFormLoggedIn, self).__init__(*args, **kwargs)
        if restaurant:
            self.fields['gerichte'].queryset = MenuItem.objects.filter(restaurant=restaurant)
            self.fields['rabattcode'].queryset = SpecialOffer.objects.filter(restaurant=restaurant)
            self.fields['rabattcode'].label_from_instance = lambda obj: f"{obj.code} - {obj.description[:30]}"

