from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from .models import UserProfile, UserMember
from .utils import send_sms


@shared_task
def notify_passport_expiry():
    # Your code to check for expiring passports and send emails
    six_months_from_now = now().date() + timedelta(days=6*30) # Approximation
    expiring_passports = UserMember.objects.filter(expiry_date__lt=six_months_from_now)

    for passport in expiring_passports:
        user = passport.user
        days_until_expiry = (passport.expiry_date - now().date()).days
        member_name = passport.first_name + " " + passport.last_name
        user_name = user.first_name + " " + user.last_name
        expiry_date = passport.expiry_date
        message = (
            f"Hello {user_name},\n\n"
            f"{member_name}'s membership is set to expire on {expiry_date}. "
            f"That's in {days_until_expiry} days from today.\n\n"
            "Please consider renewing your member's passport to continue enjoying our services.\n\n"
            "Onvigo Support Team"
        )
        send_mail(
            'Passport Expiry Notification',
            message,
            'asadeque@gmail.com',
            [user.email],
            fail_silently=False,
        )
        send_sms(
            message,
            [user.userprofile.phone]
        )
    pass
