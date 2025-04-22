from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import MenuItem

class MenuViewSetTest(APITestCase):
  def setUp(self):
    self.menu = MenuItem.objects.create(
      title="Test MenuItem", 
      price=50.00, 
      inventory=10
    )
    self.url = reverse('menu-list')

  def test_get_menu_list(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_create_menu(self):
    data = {
      "title": "New MenuItem",
      "price": 30.00,
      "inventory": 5
    }
    response = self.client.post(self.url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(MenuItem.objects.count(), 2)

  def test_update_menu(self):
    url = reverse('menu-detail', args=[self.menu.id])
    data = {
      "title": "Updated MenuItem",
      "price": 60.00,
      "inventory": 8
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.menu.refresh_from_db()
    self.assertEqual(self.menu.title, "Updated MenuItem")

  def test_delete_menu(self):
    url = reverse('menu-detail', args=[self.menu.id])
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(MenuItem.objects.count(), 0)