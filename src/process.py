import rasterio
from src.ndvi import calculate_ndvi

def generate_ndvi(file):

    with rasterio.open(file) as src:

        red = src.read(3)
        nir = src.read(4)

    ndvi = calculate_ndvi(nir, red)

    return ndvi