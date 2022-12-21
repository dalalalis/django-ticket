from django import forms
from django.contrib.auth import get_user_model
from tickets.models import Ticket, Event, Orders


User = get_user_model()

    
    
class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        
        
        
class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
        
        
class CreateOrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        
        
        
class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }
    
    
class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())