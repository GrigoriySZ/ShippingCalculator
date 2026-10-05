from django.db import models

class PickupPoint(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название ПВЗ'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долготоа')
    base_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=150.0,
        verbose_name='Базовые тарифная ставка (руб)'
    )
    def __str__(self):
        return f'{self.name} ({self.address})'