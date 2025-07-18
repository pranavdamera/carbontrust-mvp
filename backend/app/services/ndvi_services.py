from ai_model.ndvi_extraction import extract_ndvi
from ai_model.biomass_model import BiomassRegressor
import torch

def estimate_co2(lat, lon, start, end):
    # build EE polygon
    from shapely.geometry import Polygon
    poly = Polygon([ ... ])  # transform lat/lon to EE polygon
    df = extract_ndvi(poly, start, end)
    model = BiomassRegressor(); model.load_state_dict(torch.load('biomass_model.pt'))
    nd = torch.tensor(df['ndvi'].values.reshape(-1,1), dtype=torch.float32)
    bio = model(nd).detach().numpy().mean()
    return float(bio * 1.8)