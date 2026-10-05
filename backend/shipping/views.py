import math
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PickupPoint
from .serializers import PickupPointSerializer


def calculate_haversine_distance(lat1, lon1, lat2, lon2):
    """
    Расчет расстояния между двумя точками на Земле (в км) по формуле гаверсинусов.
    """
    R = 6371.0  # Радиус Земли в километрах

    # Перевод градусов в радианы
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c, 2)


class PickupPointView(generics.ListAPIView):
    # GET /api/points/
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer

@api_view(['POST'])
def calculate_shipping(request):
    # POST /api/calculate-shipping/
    user_lat = request.data.get('user_lat')
    user_lng = request.data.get('user_lng')
    point_id = request.data.get('point_id')

    # Валидация
    if user_lat is None or user_lng is None or point_id is None:
        return Response(
            {"error": "Обязательные поля для заполнения"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Запрашиваем точку из БД
    try: 
        point = PickupPoint.objects.get(id=point_id)

    except PickupPoint.DoesNotExist:
        return Response(
            {"error": "ПВЗ с таким id не найден"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Вычисляем расстояние
    distanc_km = calculate_haversine_distance(
        lat1=float(user_lat), 
        lon1=float(user_lng),
        lat2=point.latitude, 
        lon2=point.longitude
    )

    # Расчет итоговой цены
    price_per_km = 50.0
    total_price = float(point.base_price) + (distanc_km * price_per_km)
    
    return Response(
        {"point_name": point.name, 
         "address": point.address,
         "distance_km": distanc_km,
         "delivery_price": round(total_price, 2)}
    )