import datetime

from django.db import models


class Rate(models.Model):
    """Тариф."""
    title = models.CharField('Название тарифа', max_length=256, unique=True)
    count = models.FloatField('Стоимость тарифа')


class House(models.Model):
    """Дом."""
    address = models.CharField(max_length=256, unique=True)


class Apart(models.Model):
    """Квартира."""
    number = models.PositiveSmallIntegerField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    square = models.FloatField()


class Counter(models.Model):
    """Счётчик."""
    apart = models.ForeignKey(Apart, on_delete=models.CASCADE)


class Indications(models.Model):
    """Показания счетчика с учетом месяца."""
    counter = models.ForeignKey(Counter, on_delete=models.CASCADE)
    indications = models.FloatField()
    date = models.CharField(
        'Месяц и год',
        max_length=7,
        default=datetime.datetime.now().strftime('%m.%Y').replace('0', '')
    )


class DateRent(models.Model):
    """Хранение данных о квартплате по квартирам."""
    apart = models.ForeignKey(Apart, on_delete=models.CASCADE)
    count = models.IntegerField(null=True)
    date = models.CharField(
        'Месяц и год',
        max_length=7,
        null=True
    )
