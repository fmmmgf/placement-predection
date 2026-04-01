import streamlit as st
import pickle
st.title("Placement Prediction App")

model = pickle.load(open(r"C:\Users\DELL\Downloads\model .pkl", "rb"))
scaler = pickle.load(open(r"C:\Users\DELL\Downloads\scaler.pkl", "rb"))

cgpa = st.number_input("Enter CGPA")
iq = st.number_input("Enter IQ")

if st.button("Predict"):
    # ✅ SCALE INPUT (THIS IS THE FIX)
    scaled_input = scaler.transform([[cgpa, iq]])


    prediction = model.predict(scaled_input)

    st.write("Prediction value:", prediction)

    if prediction[0] == 1:
        st.success("Student Will Be Placed")
    else:
        st.error("Student Will Not Be Placed")
