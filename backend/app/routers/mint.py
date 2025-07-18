from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.nft_service import mint_credit

class MintReq(BaseModel):
    to_address: str
    metadata_cid: str

class MintRes(BaseModel):
    tx_hash: str

router = APIRouter()

@router.post('/', response_model=MintRes)
def mint(r: MintReq):
    try:
        tx = mint_credit(r.to_address, r.metadata_cid)
        return MintRes(tx_hash=tx)
    except Exception as e:
        raise HTTPException(500, str(e))