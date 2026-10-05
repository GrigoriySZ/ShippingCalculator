from django.urls import path
from .views import PickupPointView, calculate_haversine_distance

urlpatterns = [
    path('points/', PickupPointView.as_view(), name='point-list'),
    path('calculate-shipping/', calculate_haversine_distance, name='calculate-shipping')
]
