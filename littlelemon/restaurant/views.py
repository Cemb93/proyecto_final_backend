from rest_framework import viewsets, generics
from .models import MenuItem, Reservations
from .serializer import MenuItemSerializer, ReservationsSerializer
# from rest_framework.permissions import IsAuthenticated

# Lista y creación de menús (GET y POST)
class MenuItemsView(viewsets.ModelViewSet):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

# Operaciones sobre un solo menú (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  # permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class ReservationsViewSet(viewsets.ModelViewSet):
  queryset = Reservations.objects.all()
  serializer_class = ReservationsSerializer