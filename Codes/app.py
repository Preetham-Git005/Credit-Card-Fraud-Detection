import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("fraud_model_xgb1.pkl")

st.title("💳 Credit Card Fraud Detection")
st.subheader("Detect whether a transaction is fraudulent")

# Input Mode
input_mode = st.radio("Select Input Method", ["Manual Input", "Comma-Separated Input"])

# Manual Input Mode
if input_mode == "Manual Input":
    st.write("Enter transaction details below (V1 to V28 + Amount):")
    v_features = [st.number_input(f"V{i}", value=0.0, format="%.6f") for i in range(1, 29)]
    amount = st.number_input("Transaction Amount", value=0.0, format="%.2f")
    input_data = np.array(v_features + [amount]).reshape(1, -1)

# Comma-Separated Input Mode
elif input_mode == "Comma-Separated Input":
    input_str = st.text_area("Enter comma-separated values (can include 'Time'):", height=100)
    try:
        values = list(map(float, input_str.strip().split(',')))

        # If 'Time' is included (30 features), drop it
        if len(values) == 30:
            values = values[1:]

        if len(values) != 29:
            st.warning("⚠️ Please enter exactly 29 values (V1–V28 + Amount).")
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
        pred = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if pred == 1:
            st.error(f"⚠️ Fraudulent Transaction Detected! (Probability: {prob:.4f})")
        else:
            st.success(f"✅ Transaction is Legitimate. (Probability of Fraud: {prob:.4f})")