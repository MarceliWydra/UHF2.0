from django.contrib import admin

# Register your models here.
from registration.models import Participant, Ticket

admin.site.register(Participant)
admin.site.register(Ticket)