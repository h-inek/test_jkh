from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    HouseAPI, ApartAPI, CounterAPI, IndicationsAPI, DateRentAPI, RateAPI,
    rent_for_house
)

router = DefaultRouter()
router.register('house', HouseAPI)
router.register('apart', ApartAPI)
router.register('counter', CounterAPI)
router.register('inducations', IndicationsAPI)
router.register('rent', DateRentAPI)
router.register('rate', RateAPI)


urlpatterns = [
    path('', include(router.urls)),
    path('rent-for-house/', rent_for_house)
]
