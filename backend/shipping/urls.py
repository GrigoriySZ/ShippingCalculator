from django.urls import path
from .views import PickupPointView, calculate_shipping

urlpatterns = [
    path('points/', PickupPointView.as_view(), name='point-list'),
    path('calculate-shipping/', calculate_shipping, name='calculate-shipping')
]
