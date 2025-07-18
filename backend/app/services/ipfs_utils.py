import os
from pinata import PinataPy

pinata = PinataPy(os.getenv('PINATA_API_KEY'), os.getenv('PINATA_API_SECRET'))

def upload_json(data: dict) -> str:
    res = pinata.pin_json_to_ipfs(data)
    return res['IpfsHash']