import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Function to predict heart disease probability
def predict_heart_disease(age, gender, cholesterol, smoker):
    # Pre-trained model (dummy model for demonstration purposes)
    model = LogisticRegression()
    # Dummy feature engineering (in real-world scenario, you would do proper feature engineering)
    features = np.array([[age, gender, cholesterol, smoker]])
    # Dummy prediction (in real-world scenario, you would use the trained model)
    prediction = model.predict_proba(features)[:, 1]
    return prediction[0]

# Main function to run the Streamlit app
def main():
    st.title("Heart Health Predictor")

    # Input fields for user data
    age = st.slider("Age", min_value=18, max_value=100, value=50)
    gender = st.radio("Gender", options=["Male", "Female"])
    cholesterol = st.number_input("Cholesterol Level", min_value=50, max_value=400, value=200)
    smoker = st.checkbox("Smoker")

    # Convert gender to numerical value (for demonstration purposes)
    gender_numeric = 1 if gender == "Male" else 0

    # Predict heart disease probability
    if st.button("Predict"):
        probability = predict_heart_disease(age, gender_numeric, cholesterol, smoker)
        st.write(f"Probability of having heart disease: {probability:.2f}")

# Run the app
if __name__ == "__main__":
    main()
