from rest_framework import serializers
from api.models import CryptoCurrency

class GetAllCoinsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ('currency_symbol',)

class GetAllCurrencyData(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ('id', 'currency_symbol', 'currency_name', 'date', 'txVolume', 'price')