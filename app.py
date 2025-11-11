import streamlit as st
import numpy as np
import pickle
import bz2
import orange

# Fungsi load model aman
def load_orange_model(path):
    try:
        # coba sebagai file kompresi bz2
        with bz2.BZ2File(path, "rb") as f:
            return pickle.load(f)
    except OSError:
        # kalau gagal, berarti bukan bz2 → coba pickle biasa
        with open(path, "rb") as f:
            return pickle.load(f)

# === Load model Orange ===
model_path = "model/diabetes_model.pkcls"
model = load_orange_model(model_path)

st.title("🩺 Prediksi Risiko Diabetes")

st.write("Masukkan data berikut untuk memprediksi risiko diabetes Anda.")

# Input user
pregnancies = st.number_input("Jumlah Kehamilan", 0, 20, 1)
glucose = st.number_input("Kadar Glukosa", 0, 300, 120)
blood_pressure = st.number_input("Tekanan Darah (mm Hg)", 0, 200, 70)
skin_thickness = st.number_input("Ketebalan Kulit (mm)", 0, 100, 20)
insulin = st.number_input("Kadar Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.number_input("Usia", 10, 100, 30)

if st.button("Prediksi"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    prediction = model(input_data)[0]
    if prediction == 1:
        st.error("⚠️ Anda berisiko terkena diabetes.")
    else:
        st.success("✅ Anda tidak berisiko diabetes.")

