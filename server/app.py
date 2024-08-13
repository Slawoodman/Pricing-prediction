import streamlit as st
import joblib
import numpy as np
import os
import base64
from styles.background import wallpaper

model = joblib.load("model/house_prices_model.pkl")
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


background_image_path = os.path.join(current_dir, "assets", "home.jpg")
background_image = get_base64_of_bin_file(background_image_path)

background_image_style = wallpaper(background_image)

st.markdown(background_image_style, unsafe_allow_html=True)

st.markdown('<div class="content">', unsafe_allow_html=True)

st.markdown('<div class="title">House Prices Estimator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Advanced Regression Techniques</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<div class="input-label">Overall Quality</div>', unsafe_allow_html=True
    )
    overall_qual = st.number_input(
        "Overall Quality",
        min_value=1,
        max_value=10,
        value=5,
        key="overall_qual",
        label_visibility="collapsed",
    )

    st.markdown('<div class="input-label">Year Built</div>', unsafe_allow_html=True)
    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2024,
        value=2000,
        key="year_built",
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="input-label">Total Basement Area (sq ft)</div>',
        unsafe_allow_html=True,
    )
    total_bsmt_sf = st.number_input(
        "Total Basement Area (sq ft)",
        min_value=0,
        value=1000,
        key="total_bsmt_sf",
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="input-label">Living Area (sq ft)</div>', unsafe_allow_html=True
    )
    gr_liv_area = st.number_input(
        "Living Area (sq ft)",
        min_value=500,
        value=1000,
        key="gr_liv_area",
        label_visibility="collapsed",
    )

with col2:
    st.markdown('<div class="input-label">Garage Cars</div>', unsafe_allow_html=True)
    garage_cars = st.number_input(
        "Garage Cars",
        min_value=0,
        max_value=4,
        value=2,
        key="garage_cars",
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="input-label">Full Bathrooms Above Ground</div>',
        unsafe_allow_html=True,
    )
    full_bath = st.number_input(
        "Full Bathrooms Above Ground",
        min_value=0,
        max_value=3,
        value=1,
        key="full_bath",
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="input-label">Number of Fireplaces</div>', unsafe_allow_html=True
    )
    fireplaces = st.number_input(
        "Number of Fireplaces",
        min_value=0,
        max_value=3,
        value=1,
        key="fireplaces",
        label_visibility="collapsed",
    )

    st.markdown('<div class="input-label">Year Remodeled</div>', unsafe_allow_html=True)
    year_remod_add = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2024,
        value=2000,
        key="year_remod_add",
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="input-label">Lot Area (sq ft)</div>', unsafe_allow_html=True
    )
    lot_area = st.number_input(
        "Lot Area (sq ft)",
        min_value=0,
        value=5000,
        key="lot_area",
        label_visibility="collapsed",
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


input_features = np.array(
    [
        [
            overall_qual,
            year_built,
            total_bsmt_sf,
            gr_liv_area,
            garage_cars,
            full_bath,
            fireplaces,
            year_remod_add,
            lot_area,
        ]
    ]
)

if st.button("Estimate Price"):
    st.balloons()
    prediction = model.predict(input_features)
    st.markdown(
        f'<div class="prediction pulse">Estimated Price: ${prediction[0]:,.5f}</div>',
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)
