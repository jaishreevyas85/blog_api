from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        "Welcome to Blog Platform",
        "Thank you for registering!",
        "noreply@example.com",
        [user_email],
    )