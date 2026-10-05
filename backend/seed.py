import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from shipping.models import PickupPoint

def run():

    PickupPoint.objects.all().delete()

    points = [
        {
            "name": "ПВЗ Центр (Невский)",
            "address": "Невский проспект, д. 28",
            "latitude": 59.9355,
            "longitude": 30.3271,
            "base_price": 150.00
        },
        {
            "name": "ПВЗ Север (Просвещения)",
            "address": "пр. Просвещения, д. 35",
            "latitude": 60.0514,
            "longitude": 30.3341,
            "base_price": 120.00
        },
        {
            "name": "ПВЗ Юг (Московская)",
            "address": "Московский проспект, д. 195",
            "latitude": 59.8521,
            "longitude": 30.3218,
            "base_price": 180.00
        }
    ]

    for pt in points:
        PickupPoint.objects.create(**pt)

    print(f"Успешно создано {len(points)} ПВЗ!")

if __name__ == '__main__':
    run()