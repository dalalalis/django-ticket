from django.shortcuts import render


# Create your views here.
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from tickets.serializers import EventsListSerializer,CreateEventSerializer,UpdateEventSerializer,DeleteEventSerializer
from tickets.serializers import TicketListSerializer , CraeteTicketSerializer , UpdateTicketSerializer , DeleteTicketSerializer
from tickets.serializers import OrdersListSerializer , CraeteOrderSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from tickets.models import Event,Ticket,Orders




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
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    permission_classes=[AllowAny]

class TicketCreateView(CreateAPIView):
    serializer_class = CraeteTicketSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated,IsAdminUser]

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

class OrdertCreateView(CreateAPIView):
    serializer_class = CraeteOrderSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]


