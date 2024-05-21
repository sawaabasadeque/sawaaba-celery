# utils.py

from django.core.mail import send_mail
from pyfcm import FCMNotification
from django.conf import settings
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Notification:
def send_push_notification(registration_id, message_title, message_body):
    push_service = FCMNotification(api_key=settings.FCM_DJANGO_SETTINGS["FCM_SERVER_KEY"])

    registration_ids = [registration_id]

    data_message = {
        "title": message_title,
        "body": message_body,
    }

    result = push_service.notify_multiple_devices(registration_ids=registration_ids, data_message=data_message)

    # Handle the result as needed
    print(result)

# TWILLO NOTIFICATION:
def send_sms(message_body, to_phone):
    load_dotenv()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    client.messages.create(
         body=message_body,
         from_='+16592229944',
         to=to_phone,
    )
