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
        fields = ['owner', 'ticketdetails', 'event','price','available','image']

class CraeteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image']

class UpdateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image']        

class DeleteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image'] 

# ............Orders...........

class OrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['seller', 'buyer', 'ticket','date_created','date_modified']

class CraeteOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['seller', 'buyer', 'ticket','date_created','date_modified']

# class UpdateOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = ['seller', 'buyer', 'ticket','date_created','date_modified']        

# class DeleteOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = ['seller', 'buyer', 'ticket','date_created','date_modified']         

