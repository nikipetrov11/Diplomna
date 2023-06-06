from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} user profile'


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    year_of_make = models.DateField()  # must be in yyyy-mm-dd format
    registration_number = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    in_service = models.BooleanField(blank=True, null=True, default=False)

    @property
    def has_user(self):
        return bool(self.user)

    @property
    def has_events(self):
        return bool(Event.objects.filter(car_id=self.id))

    def __str__(self):
        return f'{self.maker} {self.model} - {self.registration_number}'

    def clean(self):
        """
        Validation for unique car registration number
        """
        try:
            obj = Car.objects.get(registration_number=self.registration_number)
        except Car.DoesNotExist:
            return

        if self.pk != obj.pk:
            raise ValidationError('A car with this registration number already exists in the system!')

    def get_events(self):
        return list(Event.objects.filter(car_id=self.id).order_by('-created_at'))


class Event(models.Model):
    km_of_car = models.IntegerField()
    event_text = models.TextField()
    periodic_event = models.BooleanField()
    next_date = models.DateField(blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    request_text = models.TextField()
    is_seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def has_user(self):
        return bool(self.user)

    def toggle_seen(self):
        self.is_seen = not self.is_seen
        self.save()


class InvitedUserCarRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_registration_number = models.CharField(max_length=8)
    other_info = models.TextField(blank=True, null=True)


class ContactFormModel(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    text = models.TextField()
