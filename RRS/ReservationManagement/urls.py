from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, create_reservation

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/reservation/', create_reservation, name='create-reservation'),
]