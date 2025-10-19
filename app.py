import streamlit as st
import pandas as pd
import joblib  # use joblib instead of pickle

# Load trained model using joblib
loaded_model = joblib.load("C:/Users/Benjamin/Desktop/DIVINE/house_price_model_small.joblib")  # compressed/smaller model

# Load dataset for visualization
df = pd.read_csv("USA_Housing.csv")

# Prediction function
def predict_house_price(income, age, rooms, bedrooms, population):
    new_data = pd.DataFrame([{
        'Avg. Area Income': income,
        'Avg. Area House Age': age,
        'Avg. Area Number of Rooms': rooms,
        'Avg. Area Number of Bedrooms': bedrooms,
        'Area Population': population
    }])
    prediction = loaded_model.predict(new_data)
    return prediction[0]

# Streamlit UI
st.title("🏠 USA Housing Price Prediction")

# Sidebar for user input
st.sidebar.header("Input Features for Prediction")
income = st.sidebar.number_input("Average Area Income", 10000.0, 200000.0, 79545.0)
age = st.sidebar.number_input("Average Area House Age", 0.0, 50.0, 5.68)
rooms = st.sidebar.number_input("Average Number of Rooms", 1.0, 20.0, 7.0)
bedrooms = st.sidebar.number_input("Average Number of Bedrooms", 1.0, 10.0, 4.0)
population = st.sidebar.number_input("Area Population", 1000.0, 100000.0, 23086.0)

# Prediction button
if st.button("Predict House Price"):
    price = predict_house_price(income, age, rooms, bedrooms, population)

    st.success(f"💰 Predicted House Price: RWF {price:,.2f}")

