# travel/models.py

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields of the build-in User Model
    phone = models.CharField(max_length=15, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=[
        ('Individual', 'Individual'),
        ('Family', 'Family'),
        ('Group', 'Group'),
        ('Other', 'Other'),
        ], default='Family')
    status = models.CharField(max_length=10, choices=[
        ('New', 'New'),
        ('Agent', 'Agent'),
        ('Deleted', 'Deleted'),
        ('Other', 'Other'),
        ], default='New')
    
class UserMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    nationality = CountryField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=120, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ], default='Male')
    passport_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    passport_type = models.CharField(max_length=20, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    issue_country = CountryField(blank=True, null=True)
    issue_authourity = models.CharField(max_length=120, blank=True, null=True)
    passport_photo = models.ImageField(upload_to='passport_photos', blank=True, null=True)
    agent_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, default='Valid')
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['first_name', 'last_name', 'date_of_birth', 'nationality']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date_of_birth} - {self.passport_number} - {self.expiry_date} - {self.status}"
    
class MemberFile(models.Model):
    user_member = models.ForeignKey(UserMember, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, blank=True, null=True)
    file_path = models.FileField(upload_to='member_files', blank=True, null=True)
    file_type= models.CharField(max_length=120, blank=True, null=True)
    file_size= models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, default='Valid')
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

class AirTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=20, choices=[
        ('Air-Ticket', 'Air-Ticket'),
        ('Hotel', 'Hotel'),
        ('Car', 'Car'),
        ('Other', 'Other'),
        ], default='Air-Ticket')
    trip_type = models.CharField(max_length=20, choices=[
        ('Round-Trip', 'Round-Trip'),
        ('Oneway', 'Oneway'),
        ('Multi-city', 'Multi-city'),
        ], default='Round-Trip')
    ticket_class = models.CharField(max_length=35, choices=[
        ('Economy', 'Economy'), 
        ('Premium-Economy', 'Premium-Economy'),
        ('Business', 'Business'),
        ('Premium-Business', 'Premium-Business'),
        ('First-Class', 'First-Class'),
        ('Other', 'Other'),
        ], default='Economy')
    adult_no = models.IntegerField(default=1)
    child_no = models.IntegerField(default=0)
    infant_no = models.IntegerField(default=0)
    departure_city = models.CharField(max_length=120)
    destination_city = models.CharField(max_length=120)
    departure_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    is_cancel = models.BooleanField(default=False)
    is_modify = models.BooleanField(default=False)
    stops = models.IntegerField(default=1)
    alternate_days = models.IntegerField(default=0)
    message = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Created', 'Created'), # By Member
        ('Ordered', 'Ordered'), # By Member
        ('Paid', 'Paid'), # By Auto Signal
        ('Cancelled', 'Cancelled'), # By Member
        ('Rejected', 'Rejected'), # By Airline
        ('Travelled', 'Travelled'), # By Auto Signal
        ('Deleted', 'Deleted'), # By Member
        ('Other', 'Other')
    ], default='Created')
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.departure_city} on {self.departure_date} to {self.destination_city} - {self.status}"
    
class AirTicketMember(models.Model):
    air_ticket = models.ForeignKey(AirTicket, on_delete=models.CASCADE)
    user_member = models.ForeignKey(UserMember, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Valid')
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['air_ticket', 'user_member']

class AirTicketTransaction(models.Model):
    air_ticket = models.ForeignKey(AirTicket, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=120)
    flight_details = models.CharField(max_length=255, blank=True, null=True)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    minus_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, default='Valid')
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    @property
    def net_amount(self):
        return self.gross_amount + self.add_amount - self.minus_amount
    
    @property
    def balance(self):
        return self.gross_amount + self.add_amount - self.minus_amount - self.paid_amount