import streamlit as st
import numpy as np
import pandas as pd




def main():
    st.title("Heart Health Predictor")


    age = st.slider("Age", min_value=18, max_value=100, value=50)
    gender = st.radio("Gender", options=["Male", "Female"])
    cholesterol = st.number_input("Cholesterol Level", min_value=50, max_value=400, value=200)
    smoker = st.checkbox("Smoker")


    gender_numeric = 1 if gender == "Male" else 0



if __name__ == "__main__":
    main()
