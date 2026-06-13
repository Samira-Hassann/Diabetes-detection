import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diabetes_model.pkl")

# Title
st.title("🩺 Diabetes Prediction App")
st.subheader("Enter patient information below:")

# Inputs
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Predict"):

    data = pd.DataFrame({
        "Pregnancies":[pregnancies],
        "Glucose":[glucose],
        "BloodPressure":[blood_pressure],
        "SkinThickness":[skin_thickness],
        "BMI":[bmi],
        "DiabetesPedigreeFunction":[dpf],
        "Age":[age]
    })

    probability = model.predict_proba(data)[0][1]

    prediction = int(probability >= 0.35)

    st.write(f"Probability: {probability:.2%}")

    if prediction == 1:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")



