from web3 import Web3
from eth_account import Account
from ..models import CryptoAddress

infura_url = "https://mainnet.infura.io/v3/a5aa8b36d1b04fd089148edb5278d166"

web3 = Web3(Web3.HTTPProvider(infura_url))

class Ethereum:
    def isConnected():
        bConnect = web3.isConnected()
        return bConnect

    def gen_addr(self):
        newWallet = web3.eth.account.create()
        address = newWallet.address
        priv_key = newWallet.privateKey.hex()
        newCryptoAddress = CryptoAddress(crypto_type = 'eth', crypto_address = address, crypto_priv_key = priv_key)
        newCryptoAddress.save()
        return address, priv_key

    def search_private_key(self, address):
        try:
            search_result = CryptoAddress.objects.get(crypto_type = 'eth', crypto_address=address)
        except CryptoAddress.DoesNotExist:
            search_result = None
        
        return search_result