from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

from .models import House, Apart, Counter, Indications, DateRent, Rate
from .serialiers import (
    HouseSerializer, ApartSerializer, CounterSerializer, IndicationsSerializer,
    DateRentSerializer, RateSerializer, rent
)


class HouseAPI(viewsets.ModelViewSet):
    """Вью дома."""
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [AllowAny, ]


class ApartAPI(viewsets.ModelViewSet):
    """Вью квартиры."""
    queryset = Apart.objects.all()
    serializer_class = ApartSerializer
    permission_classes = [AllowAny, ]


class CounterAPI(viewsets.ModelViewSet):
    """Вью счетчика."""
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    permission_classes = [AllowAny, ]


class IndicationsAPI(viewsets.ModelViewSet):
    """Вью показания счетчика."""
    queryset = Indications.objects.all()
    serializer_class = IndicationsSerializer
    permission_classes = [AllowAny, ]


class DateRentAPI(viewsets.ModelViewSet):
    """Вью данных о квартплате."""
    queryset = DateRent.objects.all()
    serializer_class = DateRentSerializer
    permission_classes = [AllowAny, ]


class RateAPI(viewsets.ModelViewSet):
    """Вью тарифа."""
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [AllowAny, ]


@api_view(['GET', 'POST'])
def rent_for_house(request):
    list_rent = []
    for apart in Apart.objects.filter(house_id=request.data['house']):
        rent_apart = DateRent.objects.create(
            apart=apart,
            count=rent(apart, request.data['date']),
            date=request.data['date']
        )
        rent_apart.save()
        list_rent.append(
            {'apart': rent_apart.apart.number, 'count': rent_apart.count}
        )

    return JsonResponse({'list_rent': list_rent})
