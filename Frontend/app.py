import streamlit as st
import requests

# Backend URL (Flask Server)
BASE_URL = "http://127.0.0.1:5000"

# Function to get locations from Flask API
def get_location_names():
    response = requests.get(f"{BASE_URL}/get_location_names")
    if response.status_code == 200:
        return response.json().get("locations", [])
    return []

# Function to predict house price
def predict_price(location, sqft, bhk, bath):
    data = {
        "total_sqft": sqft,
        "bhk": bhk,
        "bath": bath,
        "location": location
    }
    response = requests.post(f"{BASE_URL}/predict_home_price", data=data)
    if response.status_code == 200:
        return response.json().get("estimated_price", "Error")
    return "Error"

# Streamlit UI
st.title("🏡 House Price Prediction")

# Input Fields - Replaced sliders with input boxes
sqft = st.number_input("Enter Square Footage (sqft)", min_value=100, max_value=10000, step=10)
bhk = st.number_input("Enter BHK", min_value=1, max_value=10, step=1)  # Use number_input for BHK
bath = st.number_input("Enter Bathrooms", min_value=1, max_value=10, step=1)  # Use number_input for Bathrooms

# Load location options from API
locations = get_location_names()
location = st.selectbox("Select Location", locations)

# Predict Button
if st.button("Estimate Price"):
    if sqft and bhk and bath and location:
        estimated_price = predict_price(location, sqft, int(bhk), int(bath))
        st.success(f"🏠 Estimated Price: ₹ {estimated_price} Lakh")
    else:
        st.error("Please enter valid inputs.")

# Run the app using: `streamlit run app.py`
