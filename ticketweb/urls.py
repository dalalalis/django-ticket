from django.urls import path
from .views import index,ticket_details,add_to_cart,my_cart, remove_ticket_from_cart,profile,buy_the_cart,add_new_ticket

urlpatterns = [
    path('', index, name='index'),
    path('ticket/detail/<int:ticket_id>', ticket_details, name='ticket_details_view'),
    path('ticket/addtocart/<int:ticket_id>', add_to_cart, name='ticket_add_to_cart'),
    path('cart', my_cart, name='my_cart'),
    path('cart/checkout', buy_the_cart, name='buy_cart'),
    path('cart/remove/<int:ticket_id>', remove_ticket_from_cart, name='remove_ticket_from_cart'),
    path('profile/', profile, name='my_profile'),
    path('profile/add_ticket/', add_new_ticket, name='add_new_ticket'),
]

