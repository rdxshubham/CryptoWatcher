from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.generic import View
from api.models import CryptoCurrency
from api.views import GetAllCoins, GetRealTimeTxnFromThirdParty

# Create your views here.


class GetViewCurrencyData(View):
    def get(self, request, *args, **kwargs):
        coin_lst =[]
        coin_view = GetAllCoins.as_view({'get': 'list'})
        resp_coin_view = coin_view(request, *args, **kwargs)
        lst_resp = []
        final_dict = {}
        counter = 0
        for coin in resp_coin_view.data:
            coin_lst.append(coin['currency_symbol'])
        for coin in coin_lst:
            resp_obj = CryptoCurrency.objects.filter(currency_symbol__iexact=coin).order_by('-date')[0]

            lst_resp.append({'symbol':resp_obj.currency_symbol, 'name': resp_obj.currency_name, 'price': resp_obj.price.__str__(), 'volume': resp_obj.txVolume.__str__(), 'date': resp_obj.date.__str__()})
        for alldata in lst_resp:
            final_dict[counter] = alldata
            counter = counter + 1


        lst_json_obj = (json.dumps(lst_resp))

        return render(request, "index.html", {'table_data': final_dict})


class DetailView(View):
    def get(self, request, coin, *args, **kwargs):
        lst_resp = []
        coin_model = CryptoCurrency.objects.filter(currency_symbol__iexact=coin).order_by('-date')
        final_dict = {}
        counter = 0
        for resp_obj in coin_model:
            lst_resp.append(
                {'symbol': resp_obj.currency_symbol, 'name': resp_obj.currency_name, 'price': resp_obj.price.__str__(),
                 'volume': resp_obj.txVolume.__str__(), 'date': resp_obj.date.__str__()})

        for alldata in lst_resp:
            final_dict[counter] = alldata
            counter = counter + 1

        # real_time_data = GetRealTimeTxnFromThirdParty.as_view()
        # curr_resp = real_time_data(request, coin, *args, **kwargs).content
        #
        # curr_json = json.loads(curr_resp)
        #'curr_data': curr_json,
        return render(request, "details.html", {'table_data': final_dict, 'curr_coin': coin})

class OnlyCurrValue(View):
    def get(self, request, coin, *args, **kwargs):
        real_time_data = GetRealTimeTxnFromThirdParty.as_view()
        curr_resp = real_time_data(request, coin, *args, **kwargs).content

        return HttpResponse(curr_resp)




