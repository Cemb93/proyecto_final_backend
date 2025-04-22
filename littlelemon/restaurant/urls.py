from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menu', views.MenuItemsView)
router.register(r'reserva', views.ReservationsViewSet)


urlpatterns = [
  path('', include(router.urls)),
]