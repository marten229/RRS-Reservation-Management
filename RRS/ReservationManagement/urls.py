from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, create_reservation, ReservationListView, ReservationUpdateView, ReservationDeleteView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/reservation/', create_reservation, name='create-reservation'),
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/edit/', ReservationUpdateView.as_view(), name='reservation-edit'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'),
]