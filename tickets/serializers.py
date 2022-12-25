from rest_framework import serializers
from tickets.models import Event, Ticket, Orders
# ............Events...........
class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id','title', 'city', 'country','image','venue','startDate','startDate','endDate']


class CreateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']

class UpdateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']     

class DeleteEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']        

# ............Tickets...........

class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image','delivery']

class CraeteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image''delivery']

class UpdateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image','delivery']        

class DeleteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image','delivery'] 

# ............Orders...........

class OrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['buyer', 'ticket','date_created','date_modified']

class CraeteOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['buyer', 'ticket','date_created','date_modified']

# class UpdateOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = ['seller', 'buyer', 'ticket','date_created','date_modified']        

# class DeleteOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = ['seller', 'buyer', 'ticket','date_created','date_modified']         

