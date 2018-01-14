"""CryptoWatcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import GetAllCoins, GetRealTimeTxnFromThirdParty, GetAllCurrencyData
from watcherui.views import GetViewCurrencyData, DetailView, OnlyCurrValue
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'coins', GetAllCoins)
router.register(r'getall', GetAllCurrencyData)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', GetViewCurrencyData.as_view(), name='data'),

    url(r'^api/', include(router.urls)),
    url(r'^api/realtime/', GetRealTimeTxnFromThirdParty.as_view()),
    url(r'^real/(?P<coin>[\w\-]+)/$', OnlyCurrValue.as_view(), name='curr'),
    url(r'^detail/(?P<coin>[\w\-]+)/$', DetailView.as_view(), name='detail'),
]
