# Real Estate Price Prediction for cities in Bangalore
This project predicts real estate prices for cities in Bangalore using a Multiple Linear Regression (MLR) model. The model was trained on various independent variables like bathroom count, BHK count, location, and area in sqft. The dependent variable is the price of the property, which is predicted based on the input features.

## Key Features:
Model Accuracy: 87%
### Preprocessing Steps:
 Handling Null Values: Filled missing values appropriately.
 Location Encoding: Categorical encoding for the location column.
 Outlier Removal: Outliers removed using 1st Standard Deviation Method.
 Irrelevant Data Removal: Identified and removed irrelevant data points.
 Business-Related Outlier Removal: Removed unrealistic data (e.g., overly high or low values).
 Training and Testing split done in the ratio 80%:20%
### The model is based on Multiple Linear Regression (MLR) and predicts property prices based on:

 Independent Variables: Number of bathrooms, BHK count, location, and area in sqft.
 Dependent Variable: Price of the property.
## Web Application:
The model is wrapped in a Flask backend and integrated with a Streamlit frontend to provide a seamless user experience. The user can input property features like bathrooms, BHK, location, and area in sqft, and the application predicts the property price.

### How to Run the Application:
##### Run the Flask Backend:
python main.py
This will start the Flask backend at http://127.0.0.1:5000.

##### Run the Streamlit Frontend:
Open a new terminal and navigate to the project folder. Then run:

streamlit run Frontend.app.py
This will start the Streamlit frontend 

##### Interact with the Application:
Once both the backend and frontend are running:

Enter the property details (bathrooms, BHK, location, and area in sqft) in the Streamlit interface.
Click "Predict" to get the estimated property price.
## Technologies Used:
 Backend: Flask
 Frontend: Streamlit
 Model: Multiple Linear Regression (MLR)
#### Libraries: scikit-learn, pandas, numpy, Flask, Streamlit
## Acknowledgments:
This project uses a real estate dataset for Bangalore, and the preprocessing and model building techniques were applied to predict property prices.
