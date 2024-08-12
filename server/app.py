import streamlit as st
import joblib
import numpy as np
import base64

# Load the model
model = joblib.load("stacked_model_pipeline.pkl")

# Function to encode the image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode the background image
background_image = get_base64_of_bin_file('home.jpg')  # Replace with your image file

# Custom CSS styling with a darkened background image and neon elements
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

# Apply the custom CSS
st.markdown(background_image_style, unsafe_allow_html=True)

# App content within a div with the class "content"
st.markdown('<div class="content">', unsafe_allow_html=True)

# App title and description (now inside the content div)
st.markdown('<div class="title">House Price Estimator App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This is Abhishek\'s House Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Input fields organized in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-label">Number of Bedrooms</div>', unsafe_allow_html=True)
    number_of_bedrooms = st.number_input("", min_value=0, value=0, key='bedrooms')
    
    st.markdown('<div class="input-label">Living Area (sq ft)</div>', unsafe_allow_html=True)
    living_area = st.number_input("", min_value=1000, value=1000, key='livingarea')
    
    st.markdown('<div class="input-label">Lot Area (sq ft)</div>', unsafe_allow_html=True)
    lot_area = st.number_input("", min_value=2000, value=2000, key='lotarea')

with col2:
    st.markdown('<div class="input-label">Number of Bathrooms</div>', unsafe_allow_html=True)
    number_of_bathrooms = st.number_input("", min_value=0, value=0, key='bathrooms')
    
    st.markdown('<div class="input-label">Number of Floors</div>', unsafe_allow_html=True)
    number_of_floors = st.number_input("", min_value=0, value=0, key='floors')
    
    st.markdown('<div class="input-label">Area of the House (excluding basement) (sq ft)</div>', unsafe_allow_html=True)
    area_excluding_basement = st.number_input("", min_value=1000, value=1000, key='area_excluding_basement')

st.markdown('<div class="input-label">Number of Schools Nearby</div>', unsafe_allow_html=True)
number_of_schools_nearby = st.number_input("", min_value=0, value=0, key='numberofschools')

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Prepare the input for the model
input_features = np.array([[number_of_bedrooms, number_of_bathrooms, living_area, lot_area, number_of_floors, area_excluding_basement, number_of_schools_nearby]])

# Predict button
if st.button("Estimate Price"):
    st.balloons()
    # Perform prediction
    prediction = model.predict(input_features)
    # Display the prediction with animation
    st.markdown(f'<div class="prediction pulse">Estimated Price: ${prediction[0]:,.2f}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close the content div
