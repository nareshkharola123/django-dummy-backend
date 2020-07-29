from uuid import uuid4
from .models import User
from django.shortcuts import get_object_or_404
from .serializers import RegistrationSerializer
from rest_framework.response import Response

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings as settings
import os
from django.template.loader import render_to_string


def send_email(email, token):
    host = os.getenv("FRONT_HOST_NAME")
    message = (host + "password/?token=%s") % token
    html_content = render_to_string('users/mail.html', {"a": message})
    send_mail(
        subject='Subject here',
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=html_content
    )


# def mail_function(request):
#     subject = 'Test Mail'
#     from = 'info@domain.com'
#     to = 'to@domain.com'
#     c = Context({'email': email,
#                  'first_name': first_name})
#     html_content = render_to_string('mail/html-message.html', c)
#     txtmes = render_to_string('mail/text-message.html', c)
#     send_mail(subject,
#               txtmes,
#               from,
#               [to],
#               fail_silently=False,
#               html_message=html_content)
