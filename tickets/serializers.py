from rest_framework import serializers
from tickets.models import Event, Ticket, Orders
# ............Events...........
class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']


class CreateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','endDate']

class UpdateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']     

class DeleteEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']        

