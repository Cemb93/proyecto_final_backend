from rest_framework import viewsets
from .models import MenuItem, Reservations
from .serializer import MenuItemSerializer, ReservationsSerializer

# Create your views here. 
class MenuItemsView(viewsets.ModelViewSet):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class ReservationsViewSet(viewsets.ModelViewSet):
  queryset = Reservations.objects.all()
  serializer_class = ReservationsSerializer