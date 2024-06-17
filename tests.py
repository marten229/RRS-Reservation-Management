from django.test import TestCase, Client
from django.urls import reverse
from .models import Restaurant, User, Reservation
from django.utils import timezone
from MarketingFunctions.models import SpecialOffer, Event, Promotion
from ReviewFeedbackSystem.models import Bewertung
from UserManagement.models import User
from django.core import mail

class RestaurantListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')

    def test_restaurant_list_view(self):
        response = self.client.get(reverse('restaurant-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_list.html')
        self.assertContains(response, 'Test Restaurant')

class RestaurantDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.bewertung = Bewertung.objects.create(restaurant=self.restaurant, bewertung_gesamt=4.0, bewertung_service=4.0, bewertung_essen=4.0, bewertung_ambiente=4.0)

    def test_restaurant_detail_view(self):
        response = self.client.get(reverse('restaurant-detail', args=[self.restaurant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_detail.html')
        self.assertContains(response, 'Test Restaurant')
        self.assertEqual(response.context['durchschnittliche_bewertung_gesamt'], 4.0)

class CreateReservationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_reservation_unauthenticated(self):
        response = self.client.post(reverse('create-reservation', args=[self.restaurant.pk]), {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'telefon_nummer': '123456789',
            'datum': timezone.now().date(),
            'uhrzeit': timezone.now().time(),
            'dauer': 2,
            'anzahl_an_gästen': 4,
            'anmerkungen': 'Test Anmerkung'
        })
        self.assertEqual(response.status_code, 200) 

    def test_create_reservation_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create-reservation', args=[self.restaurant.pk]), {
            'datum': timezone.now().date(),
            'uhrzeit': timezone.now().time(),
            'dauer': 2,
            'anzahl_an_gästen': 4,
            'anmerkungen': 'Test Anmerkung'
        })
        self.assertEqual(response.status_code, 200)

class ReservationUpdateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.reservation = Reservation.objects.create(restaurant=self.restaurant, user=self.user, name='Test User', email='testuser@example.com', telefon_nummer='123456789', datum=timezone.now().date(), uhrzeit=timezone.now().time(), dauer=2, anzahl_an_gästen=4)

    def test_reservation_update_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('reservation-update', args=[self.reservation.pk]), {
            'datum': timezone.now().date(),
            'uhrzeit': timezone.now().time(),
            'dauer': 3,
            'anzahl_an_gästen': 5,
            'anmerkungen': 'Updated Anmerkung'
        })
        self.assertEqual(response.status_code, 302)

class ReservationDeleteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.reservation = Reservation.objects.create(restaurant=self.restaurant, user=self.user, name='Test User', email='testuser@example.com', telefon_nummer='123456789', datum=timezone.now().date(), uhrzeit=timezone.now().time(), dauer=2, anzahl_an_gästen=4)

    def test_reservation_delete_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('reservation-delete', args=[self.reservation.pk]))
        self.assertEqual(response.status_code, 302)

    def test_reservation_delete_sends_email(self):
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('reservation-delete', args=[self.reservation.pk]))
        self.assertEqual(len(mail.outbox), 1)

