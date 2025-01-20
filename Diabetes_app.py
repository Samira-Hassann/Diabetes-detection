import streamlit as st
import pickle
import os
if not os.path.exists("lr.pkl"):
    st.error("The model file 'lr.pkl' is missing.")
else:
    lr_model = pickle.load(open("lr.pkl", "rb"))
