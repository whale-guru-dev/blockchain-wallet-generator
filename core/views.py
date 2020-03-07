from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .modules.bitcoin import Bitcoin
from .modules.ethereum import Ethereum

# Create your views here.

def HomeView(request):
    context = {"home_view": "active"}
    return render(request, 'home.html', context)

def EthereumView(request):
    context = {"ethereum_view": "active"}
    return render(request, 'ethereum.html', context)

def BitcoinView(request):
    context = {"bitcoin_view": "active"}
    return render(request, 'bitcoin.html', context)

def AjaxReceive(request):
    # print(request.POST['value'])
    #question = Question.objects.create(question_text=request.POST['value'])
    # bitcoin = Bitcoin()
    ethereum = Ethereum()
    account = ethereum.gen_addr()
    return HttpResponse(account)

def EthAccountCreate(request):
    ethereum = Ethereum()
    account = ethereum.gen_addr()
    return JsonResponse({'address': account[0], 'priv_key': account[1]})

def EthAccountSearch(request):
    ethereum = Ethereum()
    key = request.POST['search_key']
    account = ethereum.search_private_key(key)

    if account:
        return JsonResponse({'result': 200, 'priv_key': account.crypto_priv_key})
    else:
        return JsonResponse({'result': 404})

def BtcAccountCreate(request):
    bitcoin = Bitcoin()
    account = bitcoin.gen_addr()
    return JsonResponse({'address': account[0], 'priv_key': account[1]})

def BtcAccountSearch(request):
    bitcoin = Bitcoin()
    key = request.POST['search_key']
    account = bitcoin.search_private_key(key)

    if account:
        return JsonResponse({'result': 200, 'priv_key': account.crypto_priv_key})
    else:
        return JsonResponse({'result': 404})
    

