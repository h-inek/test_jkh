from django.contrib import admin

from .models import House, Apart, Counter, Indications, Rate, DateRent


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    list_filter = ['id']
    search_fields = ['address']


@admin.register(Apart)
class ApartAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'house', 'square']
    list_filter = ['number']
    search_fields = ['number']


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ['id', 'apart']
    list_filter = ['id']
    search_fields = ['apart']


@admin.register(Indications)
class IndicationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'counter', 'indications', 'date']
    list_filter = ['id']
    search_fields = ['date']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count']
    list_filter = ['id']
    search_fields = ['title']


@admin.register(DateRent)
class DateRentAdmin(admin.ModelAdmin):
    list_display = ['id', 'apart', 'count', 'date']
    list_filter = ['id']
    search_fields = ['date']
