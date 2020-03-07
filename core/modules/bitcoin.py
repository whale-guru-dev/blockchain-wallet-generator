from pywallet import wallet
from ..models import CryptoAddress

class Bitcoin:
    def gen_addr(self):
        seed = wallet.generate_mnemonic()
        w = wallet.create_wallet(network="BTC", seed=seed, children=1)
        address = w["address"]
        priv_key = w["private_key"]
        newCryptoAddress = CryptoAddress(crypto_type = 'btc', crypto_address = address, crypto_priv_key = priv_key)
        newCryptoAddress.save()
        return address, priv_key

    def search_private_key(self, address):
        try:
            search_result = CryptoAddress.objects.get(crypto_type = 'btc', crypto_address=address)
        except CryptoAddress.DoesNotExist:
            search_result = None
        
        return search_result
    
    