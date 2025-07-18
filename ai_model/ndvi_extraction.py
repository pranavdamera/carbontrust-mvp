import ee
import pandas as pd

ee.Initialize()

def extract_ndvi(polygon, start, end):
    def mask_clouds(img):
        qa = img.select('QA60')
        mask = qa.bitwiseAnd(1<<10).eq(0).And(qa.bitwiseAnd(1<<11).eq(0))
        return img.updateMask(mask).normalizedDifference(['B8','B4']).rename('NDVI')

    col = (
        ee.ImageCollection('COPERNICUS/S2_SR')
          .filterBounds(polygon)
          .filterDate(start, end)
          .map(mask_clouds)
    )
    dates = pd.date_range(start, end, freq='MS')
    ndvi = []
    for d in dates:
        val = col.filterDate(d, d + pd.DateOffset(months=1))
                .mean()
                .reduceRegion(ee.Reducer.mean(), polygon, 10)
                .get('NDVI')
                .getInfo()
        ndvi.append({'date': d.strftime('%Y-%m-%d'), 'ndvi': val})
    return pd.DataFrame(ndvi)