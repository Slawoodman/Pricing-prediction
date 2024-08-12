import streamlit as st
import joblib
import numpy as np
import base64


model = joblib.load("house_prices_model.pkl")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


background_image = get_base64_of_bin_file("home.jpg")


background_image_style = f"""
    <style>
        .stApp {{
            background: linear-gradient(rgba(15, 15, 15, 0.8), rgba(15, 15, 15, 0.8)), url(data:image/jpg;base64,{background_image});
            background-size: cover;
            color: #00ffea;
            font-family: 'Courier New', Courier, monospace;
        }}
        .content {{
            background: rgba(15, 15, 15, 0.9);
            padding: 30px;
            border-radius: 15px;
            border: 2px solid #00ffea;
            box-shadow: 0px 0px 20px #ff00ff;
        }}
        .title {{
            font-size: 48px;
            font-weight: bold;
            color: #ff00ff;
            text-align: center;
            text-shadow: 0px 0px 10px #ff00ff;
        }}
        .subtitle {{
            font-size: 24px;
            text-align: center;
            margin-bottom: 30px;
            color: #00ffea;
            text-shadow: 0px 0px 10px #00ffea;
        }}
        .divider {{
            border-top: 2px solid #ff00ff;
            margin: 20px 0;
        }}
        .input-label {{
            font-size: 18px;
            margin-bottom: 5px;
            color: #ff00ff;
            text-shadow: 0px 0px 10px #ff00ff;
        }}
        .prediction {{
            font-size: 36px;
            color: #00ffea;
            font-weight: bold;
            text-align: center;
            text-shadow: 0px 0px 20px #00ffea;
            animation: neonGlow 2s ease-in-out infinite alternate;
        }}
        @keyframes neonGlow {{
            from {{
                text-shadow: 0 0 20px #00ffea, 0 0 30px #00ffea, 0 0 40px #ff00ff, 0 0 50px #ff00ff, 0 0 60px #ff00ff, 0 0 70px #ff00ff;
            }}
            to {{
                text-shadow: 0 0 30px #00ffea, 0 0 40px #00ffea, 0 0 50px #ff00ff, 0 0 60px #ff00ff, 0 0 70px #ff00ff, 0 0 80px #ff00ff;
            }}
        }}
        .footer {{
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #00ffea;
            text-shadow: 0px 0px 10px #00ffea;
        }}
        .pulse {{
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
    </style>
"""

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
    st.markdown('<div class="input-label">Overall Quality</div>', unsafe_allow_html=True)
    overall_qual = st.number_input("", min_value=1, max_value=10, value=5, key="overall_qual")

    st.markdown('<div class="input-label">Year Built</div>', unsafe_allow_html=True)
    year_built = st.number_input("", min_value=1800, max_value=2024, value=2000, key="year_built")

    st.markdown('<div class="input-label">Total Basement Area (sq ft)</div>', unsafe_allow_html=True)
    total_bsmt_sf = st.number_input("", min_value=0, value=1000, key="total_bsmt_sf")

    st.markdown('<div class="input-label">Living Area (sq ft)</div>', unsafe_allow_html=True)
    gr_liv_area = st.number_input("", min_value=500, value=1000, key="gr_liv_area")

with col2:
    st.markdown('<div class="input-label">Garage Cars</div>', unsafe_allow_html=True)
    garage_cars = st.number_input("", min_value=0, max_value=4, value=2, key="garage_cars")

    st.markdown('<div class="input-label">Full Bathrooms Above Ground</div>', unsafe_allow_html=True)
    full_bath = st.number_input("", min_value=0, max_value=3, value=1, key="full_bath")

    st.markdown('<div class="input-label">Number of Fireplaces</div>', unsafe_allow_html=True)
    fireplaces = st.number_input("", min_value=0, max_value=3, value=1, key="fireplaces")

    st.markdown('<div class="input-label">Year Remodeled</div>', unsafe_allow_html=True)
    year_remod_add = st.number_input("", min_value=1800, max_value=2024, value=2000, key="year_remod_add")

    st.markdown('<div class="input-label">Lot Area (sq ft)</div>', unsafe_allow_html=True)
    lot_area = st.number_input("", min_value=0, value=5000, key="lot_area")

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
        f'<div class="prediction pulse">Estimated Price: ${prediction[0]:,.2f}</div>',
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)
