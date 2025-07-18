import os, json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URI')))
with open('app/services/CarbonCreditNFT.abi.json') as f:
    ABI = json.load(f)
contract = w3.eth.contract(address=os.getenv('CONTRACT_ADDRESS'), abi=ABI)


def mint_credit(to_address, cid):
    metadata_uri = f'ipfs://{cid}'
    acct = w3.eth.account.from_key(os.getenv('PRIVATE_KEY'))
    txn = contract.functions.mintCredit(
        to_address, metadata_uri,
        # dummy metadata fields: projectName, locationHash, co2Tons, timestamp, verifierHash
        "Project", b'' , 1, int(time.time()), b''
    ).buildTransaction({
        'from': acct.address,
        'nonce': w3.eth.getTransactionCount(acct.address),
        'gasPrice': w3.toWei('20','gwei')
    })
    signed = acct.sign_transaction(txn)
    return w3.eth.sendRawTransaction(signed.rawTransaction).hex()
