from django.contrib import admin

from cars.models import Car, Event, ServiceRequest, ContactFormModel

# Register your models here.
admin.site.register(Car)
admin.site.register(Event)
admin.site.register(ServiceRequest)
admin.site.register(ContactFormModel)
