import numpy as np

def calculate_ndvi(nir, red):

    nir = nir.astype(float)
    red = red.astype(float)

    ndvi = (nir - red) / (nir + red)

    return ndvi