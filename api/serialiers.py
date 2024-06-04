import datetime

from rest_framework import serializers

from .models import House, Apart, Counter, Indications, DateRent, Rate


def rent(apart, date=datetime.datetime.now().strftime('%m.%Y').replace('0', '')):
    count_property = (
            apart.square * Rate.objects.get(title='Property').count
    )
    consumption = 0

    for counter in Counter.objects.filter(apart=apart):
        ind_now = Indications.objects.get(
            counter=counter,
            date=date
        ).indications
        if date.startswith('1'):
            ind_then = Indications.objects.get(
                counter=counter,
                date=f'12.{int(date.split(".")[1]) - 1}'
            ).indications

            consumption += ind_now - ind_then
            continue

        ind_then = Indications.objects.get(
            counter=counter,
            date=f'{int(date.split(".")[0]) - 1}.{date.split(".")[1]}'
        ).indications
        consumption += ind_now - ind_then

    count_watersupply = (
            consumption * Rate.objects.get(title='WaterSupply').count
    )

    return count_watersupply+count_property


class RateSerializer(serializers.ModelSerializer):
    """Сериализатор показаний счетчика."""

    class Meta:
        model = Rate
        fields = '__all__'


class DateRentSerializer(serializers.ModelSerializer):
    """Сериализатор рассчета квартплаты за квартиру."""
    count = serializers.CharField(required=False)

    class Meta:
        model = DateRent
        fields = '__all__'

    def create(self, validated_data):
        apart = validated_data.get('apart')
        date = datetime.datetime.now().strftime('%m.%Y').replace('0', '')
        if validated_data.get('date') is not None:
            date = validated_data.get('date')

        return DateRent.objects.create(
            apart=apart,
            count=rent(apart, date),
            date=date
        )


class IndicationsSerializer(serializers.ModelSerializer):
    """Сериализатор показаний счетчика."""

    class Meta:
        model = Indications
        fields = '__all__'


class CounterSerializer(serializers.ModelSerializer):
    """Сериализатор счетчика."""
    indications_set = IndicationsSerializer(many=True, read_only=True)

    class Meta:
        model = Counter
        fields = ('apart', 'indications_set')


class ApartSerializer(serializers.ModelSerializer):
    """Сериализатор квартиры."""
    counter_set = CounterSerializer(many=True, read_only=True)

    class Meta:
        model = Apart
        fields = ('id', 'number', 'square', 'house', 'counter_set')


class HouseSerializer(serializers.ModelSerializer):
    """Сериализатор дома."""
    apart_set = ApartSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ('id', 'address', 'apart_set')
