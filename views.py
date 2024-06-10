from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Restaurant, User, Reservation
from .forms import ReservationForm, ReservationFormLoggedIn
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

#dummy_user, created = User.objects.get_or_create(username='dummy_user', defaults={'email': 'dummy@example.com', 'password': 'dummy_password'})
# View für die Übersicht aller Restaurants
class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return Restaurant.objects.all()

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'  
    context_object_name = 'restaurant'

    def get_object(self):
        restaurant_id = self.kwargs.get('pk')
        return Restaurant.objects.get(pk=restaurant_id)
    
class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'
    context_object_name = 'restaurant'

    def get_object(self):
        restaurant_id = self.kwargs.get('pk')
        return Restaurant.objects.get(pk=restaurant_id)

def create_reservation(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReservationFormLoggedIn(request.POST)
        else:
            form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.restaurant = restaurant
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            return redirect('restaurant-detail', pk=restaurant.pk)
    else:
        if request.user.is_authenticated:
            form = ReservationFormLoggedIn()
        else:
            form = ReservationForm()
    return render(request, 'create_reservation.html', {'form': form, 'restaurant': restaurant})

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_form.html'
    context_object_name = 'reservation'

    def get_success_url(self):
        return reverse_lazy('reservation-list')

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation_confirm_delete.html'
    context_object_name = 'reservation'
    success_url = reverse_lazy('reservation-list')

