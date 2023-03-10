from django.shortcuts import render
from datetime import datetime

# Create your views here.
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from tickets.serializers import EventsListSerializer,CreateEventSerializer,UpdateEventSerializer,DeleteEventSerializer
from tickets.serializers import TicketListSerializer , CraeteTicketSerializer , UpdateTicketSerializer , DeleteTicketSerializer
from tickets.serializers import OrdersListSerializer , CraeteOrderSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from tickets.models import Event,Ticket,Orders,User




# ------------- Event VIEWS -------------

class EventListView(ListAPIView):
    serializer_class = EventsListSerializer
    def get_queryset(self):
        queryset = Event.objects.all()
        
        return queryset
    permission_classes=[AllowAny]

class EventCreateView(CreateAPIView):
    serializer_class = CreateEventSerializer
    def perform_create(self, serializer):
        serializer.save()
        permission_classes=[IsAdminUser]

class EventUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = UpdateEventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsAdminUser]

class EventDeleteView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = DeleteEventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsAdminUser]

# ------------- Ticket VIEWS -------------

class TicketListView(ListAPIView):
    serializer_class = TicketListSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        param_event_id=self.request.GET.get('event_id', None)
        if param_event_id:
            return Ticket.objects.filter(available=True, event__id=int(param_event_id), event__startDate__gt=datetime.now())
        return Ticket.objects.filter(event__startDate__gt=datetime.now())
    
class UserListedTickets(ListAPIView):
    serializer_class = TicketListSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(owner=user)
         


class TicketCreateView(CreateAPIView):
    serializer_class = CraeteTicketSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class TicketUpdateView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = UpdateTicketSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

class TicketDeleteView(DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = DeleteTicketSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

# ------------- Order VIEWS -------------

class OrderListView(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersListSerializer
    permission_classes=[AllowAny]
    def get_orderqueryset(self):
        param_ticket_id=self.request.GET.get('ticket_id', None)
        if param_ticket_id:
            return Orders.objects.filter( ticket__startDate__gt=datetime.now())
        return Orders.objects.filter(ticket__startDate__gt=datetime.now())



class OrdertCreateView(CreateAPIView):
    serializer_class = CraeteOrderSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]


