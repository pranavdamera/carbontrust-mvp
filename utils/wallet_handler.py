from web3 import Web3
import os

w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URI')))

def get_contract(abi, address):
    return w3.eth.contract(address=address, abi=abi)