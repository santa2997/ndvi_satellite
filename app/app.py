import streamlit as st
import rasterio
import numpy as np
import matplotlib.pyplot as plt

st.title("NDVI Satellite Analysis App")

uploaded = st.file_uploader("Upload GeoTIFF", type=["tif"])

if uploaded:

    with rasterio.open(uploaded) as src:

        red = src.read(3)
        nir = src.read(4)

    ndvi = (nir - red) / (nir + red)

    fig, ax = plt.subplots()

    img = ax.imshow(ndvi, cmap="RdYlGn")
    fig.colorbar(img)

    st.pyplot(fig)