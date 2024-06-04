# import os
# import django
# from django.core.exceptions import ObjectDoesNotExist
# from django.utils import timezone
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_jkh.settings')
# django.setup()
#
# import datetime
#
# from api.models import Counter, House, Apart, Rate, Indications, DateRent
#
#
# def create(house, date=datetime.datetime.now().strftime('%m.%Y').replace('0', '')):
#
#     if date is not None:
#         date = date
#     list_rent = []
#     for apart in Apart.objects.filter(house=house):
#         count_property = (
#                 apart.square * Rate.objects.get(title='Property').count
#         )
#         consumption = 0
#
#         for counter in Counter.objects.filter(apart=apart):
#             ind_now = Indications.objects.get(
#                 counter=counter,
#                 date=date
#             ).indications
#             if date.startswith('1'):
#                 ind_then = Indications.objects.get(
#                     counter=counter,
#                     date=f'12.{int(date.split(".")[1]) - 1}'
#                 ).indications
#
#                 consumption += ind_now - ind_then
#                 continue
#
#             ind_then = Indications.objects.get(
#                 counter=counter,
#                 date=f'{int(date.split(".")[0]) - 1}.{date.split(".")[1]}'
#             ).indications
#             consumption += ind_now - ind_then
#
#         count_watersupply = (
#                 consumption * Rate.objects.get(title='WaterSupply').count
#         )
#         try:
#             list_rent.append(DateRent.objects.create(
#                 apart=apart,
#                 count=count_property + count_watersupply,
#                 date=date
#             ))
#         except ObjectDoesNotExist:
#             continue
#     return list_rent
#
# print(create(1, '3.2023'))
