# 💳 Credit Card Fraud Detection App

This project is a Machine Learning-based solution to detect fraudulent credit card transactions using anonymized features (V1–V28) and transaction amount. The project includes model training, evaluation, and deployment of an interactive web app using **Streamlit**, hosted on **AWS EC2**.

---

## 📌 Features

- Trained a **Random Forest Classifier** model to detect fraudulent transactions.
- Applied **SMOTE** to resolve class imbalance.
- Evaluated models using Accuracy, Precision, Recall, F1 Score, and ROC AUC.
- Built an interactive frontend with **Streamlit**.
- Deployed the web app on **AWS EC2** for public access.
- Allows both:
  - Manual Input of V1–V28 and Amount
  - Comma-Separated Input of all features at once

---

## 🧠 Model Used

- **Random Forest Classifier**
- Dataset balanced using **SMOTE (Synthetic Minority Over-sampling Technique)**
- Dataset used: `creditcard.csv` from Kaggle

---

## 📊 Model Performance

| Metric     | Random Forest |
|------------|----------------|
| Accuracy   | 0.9995         |
| Precision  | 0.87           |
| Recall     | 0.83           |
| F1 Score   | 0.85           |
| ROC AUC    | 0.91           |

---

## 🖥️ Streamlit Web App

- Enter transaction data manually or using comma-separated values
- Predicts whether a transaction is **Fraudulent** or **Legitimate**
- Clean, simple UI built with **Streamlit**

---

## 🚀 Deployment on AWS EC2

- Ubuntu EC2 instance used for deployment
- Port 8501 opened to allow external access
- Used `nohup` to keep the Streamlit app running in the background
- App URL: `http://<your-ec2-public-ip>:8501`

---

## 📁 Files Included

| File Name         | Description                             |
|------------------|-----------------------------------------|
| `app.py`          | Streamlit app code                      |
| `fraud_model.pkl` | Trained Random Forest model             |
| `creditcard.csv`  | Dataset (not uploaded — from Kaggle)    |
| `README.md`       | Project documentation                   |

---

## 🧑‍💼 Roles in This Project

- **Data Analyst**: Data cleaning, SMOTE balancing
- **ML Engineer**: Model Training
- **Evaluation Lead**: Evaluate the best model
- **Cloud Deployer**: AWS EC2 setup, SSH, deployment
- **Visualizer**: Created charts (heatmaps, distributions, model metrics)
- **UI Deployer**: Website UI Designer
- **Document Lead**: Report and PPT creation

---

## 🔗 Resources

- [Kaggle Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- [Streamlit Docs](https://docs.streamlit.io/)
- [AWS EC2](https://aws.amazon.com/ec2/)

---

## 🙌 Acknowledgments

Thanks to the internship program for providing this real-world simulation of roles across Data Science, Machine Learning, and Cloud Deployment.

---

## 📧 Contact

For queries, reach out via GitHub Issues.
