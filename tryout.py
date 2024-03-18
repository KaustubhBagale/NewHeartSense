import streamlit as st
import numpy as np
import pandas as pd



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


# Run the app
if __name__ == "__main__":
    main()
