from django.shortcuts import render


# Create your views here.
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from tickets.serializers import EventsListSerializer,CreateEventSerializer,UpdateEventSerializer,DeleteEventSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from tickets.models import Event,Ticket,Orders

# from recipes.permissions import IsCreator


# ------------- RECIPE VIEWS -------------

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