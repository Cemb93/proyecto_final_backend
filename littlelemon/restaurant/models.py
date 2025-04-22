from django.db import models

# Create your models here.
class MenuItem(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()

  def get_item(self):
    return f'{self.title} : {str(self.price)}'
  
  def __str__(self):
    return f'{self.title} : {str(self.price)}'

class Reservations(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.IntegerField()
  booking_date = models.DateTimeField()

  def __str__(self):
    return self.name