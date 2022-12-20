from django.contrib import admin
from tickets.models import Ticket, Orders , Event
# Register your models here.
admin.site.register([Event, Ticket,Orders])