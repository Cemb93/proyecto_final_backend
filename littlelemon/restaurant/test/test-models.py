from django.test import TestCase
from ..models import MenuItem, Reservations

class MenuModelTest(TestCase):
  def setUp(self):
    MenuItem.objects.create(
      title="Test MenuItem", 
      price=50.00, 
      inventory=10
    )

  def test_menu_creation(self):
    menu = MenuItem.objects.get(title="Test MenuItem")
    self.assertEqual(menu.title, "Test MenuItem")
    self.assertEqual(menu.price, 50.00)
    self.assertEqual(menu.inventory, 10)

  def test_menu_str_representation(self):
    menu = MenuItem.objects.get(title="Test MenuItem")
    self.assertEqual(str(menu), "Test MenuItem : 50.00")

class ReservasModelTest(TestCase):
  def setUp(self):
    Reservations.objects.create(
      name="John Doe", 
      no_of_guests=4, 
      booking_date="2025-04-22T10:00:00Z"
    )

  def test_reservas_creation(self):
    reserva = Reservations.objects.get(name="John Doe")
    self.assertEqual(reserva.name, "John Doe")
    self.assertEqual(reserva.no_of_guests, 4)
    self.assertEqual(str(reserva.booking_date), "2025-04-22 10:00:00+00:00")

  def test_reservas_str_representation(self):
    reserva = Reservations.objects.get(name="John Doe")
    self.assertEqual(str(reserva), "John Doe")