from celery import shared_task
from todo_api.models import Task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from app.settings import DEFAULT_FROM_EMAIL


@shared_task
def check_task_deadlines_missed():
    current_time = timezone.now()
    tasks = Task.objects.filter(deadline__lte=current_time, completed=False)
    for task in tasks:
        email = task.user.email
        message = f"The deadline ('{task.deadline}') for task '{task.description}' was missed."
        send_notification.delay("Deadline", email, message)


@shared_task
def check_task_deadlines_approaching():
    current_time = timezone.now()
    two_hour_later = current_time + timedelta(hours=2)
    tasks = Task.objects.filter(
        deadline__gt=current_time, deadline__lte=two_hour_later, completed=False
    )
    for task in tasks:
        email = [task.user.email]
        message = f"The deadline ('{task.deadline}') for task '{task.description}' is approaching. Less than 2 hours left."
        send_notification.delay("Deadline approaching", email, message)


@shared_task
def send_notification(subject, email, message):
    send_mail(subject, message, DEFAULT_FROM_EMAIL, [email])
