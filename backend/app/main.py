from fastapi import FastAPI
from app.routers import estimate, mint

app = FastAPI(title='CarbonTrust API')
app.include_router(estimate.router, prefix='/estimate')
app.include_router(mint.router, prefix='/mint')