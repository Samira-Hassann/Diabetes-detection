# 🩺 Diabetes Analysis & Prediction Project

An end-to-end Machine Learning & Deep Learning project focused on analyzing medical diagnostic data and predicting the likelihood of diabetes in patients.

## 🌐 Quick Links
- 🚀 **Live Demo App:** [Streamlit Web App](https://diabetes-detection-2wuzwqd2pre6yskix84xet.streamlit.app/)
- 📓 **Kaggle Notebook:** [Diabetes Analysis & Prediction Notebook](https://www.kaggle.com/code/samoura/diabetes-analysis-prediction-using-ml-and-dl/notebook)

---

## 📌 Project Overview
This project processes clinical indicators such as Glucose levels, BMI, Age, and Blood Pressure to detect early-stage diabetes. Key highlights include:
- **Data Cleaning & Imputation:** Handled missing/biologically impossible zero values using KNN Imputer and statistical mean.
- **Outlier Capping:** Applied Winsorization thresholds to preserve sample size while capping extreme variances.
- **Class Imbalance Management:** Integrated resampling techniques (SMOTE/undersampling) and tuned class weights.
- **Clinical Threshold Optimization:** Decision threshold is set to **`0.35`** to maximize Recall (84.3%) and minimize False Negatives for safer medical screening.

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Data Processing & ML:** Pandas, NumPy, Scikit-Learn, XGBoost, LightGBM, Imbalanced-Learn
- **Deep Learning:** TensorFlow / Keras
- **Web App & Deployment:** Streamlit Cloud

---

## 📁 Repository Structure
```text
├── Diabetes_app.py                  # Streamlit application script
├── requirements.txt        # Python package dependencies
├── diabetes_model.pkl   # Trained model 
└── README.md               # Project documentation
