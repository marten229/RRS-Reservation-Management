# ReservationManagement/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Reservation

@shared_task
def send_reservation_reminders():
    now = timezone.now()
    reminder_time = now + timedelta(hours=24)
    reservations = Reservation.objects.filter(datum=reminder_time.date(), uhrzeit__hour=reminder_time.hour)

    for reservation in reservations:
        subject = 'Erinnerung: Ihre Reservierung im Restaurant'
        message = (
            f"Hallo {reservation.user.first_name},\n\n"
            f"Dies ist eine Erinnerung an Ihre Reservierung im Restaurant {reservation.restaurant.name} "
            f"am {reservation.datum} um {reservation.uhrzeit}.\n\n"
            f"Wir freuen uns auf Ihren Besuch!"
        )
        recipient_list = [reservation.user.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
