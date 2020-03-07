from django.urls import path, include
from .views import HomeView, EthereumView, BitcoinView, EthAccountCreate, EthAccountSearch, BtcAccountCreate, BtcAccountSearch

app_name = 'core'

urlpatterns = [
    path('', HomeView, name="home_view"),
    path('ethereum', EthereumView, name="ethereum_view"),
    path('bitcoin', BitcoinView, name="bitcoin_view"),
    path('btc_account_create', BtcAccountCreate, name="BtcAccountCreate"),
    path('btc_account_search', BtcAccountSearch, name="BtcAccountSearch"),
    path('eth_account_create', EthAccountCreate, name="EthAccountCreate"),
    path('eth_account_search', EthAccountSearch, name="EthAccountSearch")
]