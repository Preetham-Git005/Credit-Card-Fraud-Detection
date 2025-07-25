import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection App")
st.subheader("Detect whether a transaction is fraudulent or not")

# Input Mode
input_mode = st.radio("Select Input Method", ["Manual Input", "Comma-Separated Input"])

if input_mode == "Manual Input":
    st.write("Enter transaction details below:")
    v_features = [st.number_input(f"V{i}", value=0.0, format="%.5f") for i in range(1, 29)]
    amount = st.number_input("Transaction Amount", value=0.0, format="%.2f")
    input_data = np.array(v_features + [amount]).reshape(1, -1)

elif input_mode == "Comma-Separated Input":
    input_str = st.text_area("Enter comma-separated values for V1 to V28 and Amount (29 values):", height=100)
    try:
        values = list(map(float, input_str.strip().split(',')))
        if len(values) != 29:
            st.warning("⚠️ Please enter exactly 29 values (V1-V28 and Amount).")
            input_data = None
        else:
            input_data = np.array(values).reshape(1, -1)
    except ValueError:
        st.error("⚠️ Please enter valid numeric values only.")
        input_data = None

# Prediction
if st.button("Predict Fraud"):
    if input_data is None:
        st.error("Invalid input. Please correct the input values.")
    else:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error("⚠️ Fraudulent Transaction Detected!")
        else:
            st.success("✅ Transaction is Legitimate.")