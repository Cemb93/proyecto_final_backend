from rest_framework import serializers
from .models import MenuItem, Reservations

class MenuItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = MenuItem
    fields = '__all__'
    
class ReservationsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Reservations
    fields = '__all__'