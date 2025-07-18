from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ndvi_service import estimate_co2

class Req(BaseModel):
    latitude: float; longitude: float
    start_date: str; end_date: str

class Res(BaseModel):
    co2_sequestered_tons: float

router = APIRouter()

@router.post('/', response_model=Res)
def get_co2(r: Req):
    try:
        val = estimate_co2(r.latitude, r.longitude, r.start_date, r.end_date)
        return Res(co2_sequestered_tons=val)
    except Exception as e:
        raise HTTPException(500, str(e))