from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError

 
class Event(models.Model):
    title = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField(help_text='Product Image', upload_to='events', blank=True)  
    venue = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
   
    def __str__(self):
        return f'{self.startDate}'
   
 
class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_tickets")
    ticketdetails= models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="ticket_event")
    price = models.FloatField()
    available = models.BooleanField()
    image = models.ImageField(help_text='Product Image', upload_to='tickets', blank=True) 
    class Delivery_Method(models.TextChoices):
        physical = "Physical"
        immediate = "immediate"
        twentyfourhours = "Twenty_Four_Hours"
        threedays = "Three_Days"
        oneweek = "One_Week"
    delivery = models.CharField(max_length=100, choices=Delivery_Method.choices,default = "immediate")

    def __str__(self):
        return f'{self.ticketdetails, self.event,self.owner, self.price, self.delivery}'




class Orders(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="order")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified =models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f'{self.buyer ,self.ticket, self.date_created, self.date_modified}'

class Profile(models.Model):
    user_name =models.OneToOneField(User,on_delete=models.CASCADE,primary_key="True")
    civilid = models.PositiveIntegerField()    
