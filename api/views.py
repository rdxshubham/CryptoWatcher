from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from rest_framework.views import APIView
from django.conf import settings
import requests, json

from api.models import CryptoCurrency
from api.serializers import GetAllCoinsSerializer, GetAllCurrencyData


class ThridPartyApi:
    def __init__(self, coin_symbol):
        self.coin_symbol = coin_symbol

    def get_real_time(self):
        url = "https://www.alphavantage.co/query"
        querystring = {"function": "DIGITAL_CURRENCY_INTRADAY", "symbol": self.coin_symbol, "market": "USD",
                       "apikey": settings.API_KEY}
        response = requests.get(url, params=querystring).json()
        last_refreshed = response['Meta Data']['7. Last Refreshed']
        return response['Time Series (Digital Currency Intraday)'][last_refreshed]


class GetAllCoins(viewsets.ModelViewSet):
    queryset = CryptoCurrency.objects.values('currency_symbol').distinct()
    serializer_class = GetAllCoinsSerializer


class GetRealTimeTxnFromThirdParty(View):
    #renderer_classes = (JSONRenderer,)
    queryset = CryptoCurrency.objects.all()
    def get(self, request, coin, *args, **kwargs):
        coin_list = []
        coin_view = GetAllCoins.as_view({'get': 'list'})
        resp_coin_view = coin_view(request, *args, **kwargs)
        real_price_dict = {}
        third_party_api_obj = ThridPartyApi(coin)
        thrid_resp = third_party_api_obj.get_real_time()
        manu_list = []
        manu_list.append(thrid_resp['1a. price (USD)'])
        manu_list.append(thrid_resp['2. volume'])
        real_price_dict.update({coin: manu_list})
        return HttpResponse(json.dumps(real_price_dict))

class GetAllCurrencyData(viewsets.ModelViewSet):
    queryset = CryptoCurrency.objects.all()
    serializer_class = GetAllCurrencyData
