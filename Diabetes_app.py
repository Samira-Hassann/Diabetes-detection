import streamlit as st
import pickle
lr_model = pickle.load(open("lr.pkl","rb"))
# App title
st.title("Diabetes detection app")

# Create input fields for numerical features
st.subheader("Fill these data:")

# Input fields for each feature
pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose Level")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin Level")
bmi = st.number_input("BMI")
diabetes_pedigree = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")



if st.button("Submit"):
    data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
    pred = lr_model.predict(data)
    
    if pred[0] == 1:
        st.success("You have Diabetes")
    else:
        st.success("You don't have Diabetes")
