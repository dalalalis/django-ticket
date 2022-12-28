from django.urls import path
from .views import index,ticket_details

urlpatterns = [
    path('', index, name='index'),
    path('ticket/detail/<int:ticket_id>', ticket_details, name='ticket_details_view'),
]

    