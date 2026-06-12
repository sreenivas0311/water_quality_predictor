# 💧 Water Quality Prediction System

A  Machine Learning application for **water quality classification** using physicochemical and biological parameters.
The system supports **manual data entry** and **Excel-based batch prediction**, and is deployed using **Streamlit** with a clean UI.

---

## 📌 Problem Statement

Water quality assessment is critical for environmental monitoring, public health, agriculture, and industrial use.
Manual evaluation using multiple parameters is complex, time-consuming, and error-prone.

This project aims to:

* Automate water quality classification
* Use Machine Learning for prediction
* Support real-time single-sample prediction
* Support bulk prediction using Excel files
* Provide a simple UI for non-technical users

The system classifies water into categories such as:

* **Good**
* **Polluted**
* **Highly Polluted**

---

## 🎯 Project Goals

* Build a **production-style ML system** (not notebook-based workflows)
* Separate experimentation from deployment
* Support both **manual input** and **file upload**
* Provide **batch prediction capability**
* Maintain a clean and deployable architecture
* Enable future API/app integration

---

## 🧠 Machine Learning Model

* Algorithm: **XGBoost Classifier**
* Input Features: **29 water quality parameters**
* Output: Water quality class label
* Model files:

  * `water_quality_xgb_model.pkl`
  * `feature_columns.pkl`
  * `label_mapping.pkl`

---

## 🧾 Input Parameters (29 Features)

1. Approx Depth
2. Temperature
3. Dissolved O2
4. pH
5. Conductivity
6. BOD
7. Nitrate N
8. Fecal Coliform
9. Total Coliform
10. Fecal Streptococci
11. Turbidity
12. Phenophelene Alkanity
13. Total Alkalinity
14. Chlorides
15. COD
16. Total Kjeldahl N
17. Amonia N
18. Hardness CaCo3
19. Calcium CaCo3
20. Magnesium CaCo3
21. Sulphate
22. Sodium
23. Total Dissolved Solids
24. Total Fixed Solids
25. Total Suspended Solids
26. Phosphate
27. Boron
28. Potassium
29. Flouride

---

## 🧩 System Modes

### 👤 User Entry Mode

* Manual entry of 29 parameters
* Real-time prediction
* Single sample inference

### 📁 Excel File Mode

* Upload `.xlsx` file
* Multiple record prediction
* Batch processing
* Output as table
* Downloadable results file

---

## 🏗️ Project Structure

```
water_quality_ml/
│
├── app.py                  # Streamlit app entry point
├── user_interface.py       # UI logic and prediction flow
├── water_quality_xgb_model.pkl
├── feature_columns.pkl
├── label_mapping.pkl
├── requirements.txt
├── README.md
└── .venv/                  # Virtual environment
```

---

## ⚙️ Environment Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 2️⃣ Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present:

```bash
pip install streamlit pandas numpy scikit-learn xgboost openpyxl
```

---

## ▶️ How to Run the Project

> ⚠️ IMPORTANT: Always run Streamlit from the virtual environment

```bash
.venv\Scripts\streamlit.exe run app.py
```

---

## 📊 How the System Works

1. User enters data OR uploads Excel file
2. Input is validated
3. Features are aligned with trained model
4. Model performs inference
5. Prediction label is generated
6. Result is displayed in UI
7. (Excel mode) Batch results are downloadable

---

## ⚠️ Model Disclaimer

This model is trained on a **limited dataset**.

* Predictions are statistical approximations
* Extreme values in a single feature may not dominate predictions
* Results should be used for **decision support only**
* Not a substitute for laboratory testing

---

## 🚀 Deployment

This project is designed for deployment using:

* **Streamlit Cloud**
* Local server deployment
* Container-based deployment (Docker – future ready)

---

## 🧱 Design Philosophy

* Production-first mindset
* Clean separation of concerns
* No notebook-based deployment
* Modular design
* Extendable architecture
* API-ready structure

---

## 🔮 Future Enhancements

* REST API (FastAPI integration)
* Database storage
* User authentication
* Role-based access
* Model versioning
* Model monitoring
* Data drift detection
* Auto retraining pipelines
* Explainable AI (SHAP/LIME)
* Cloud deployment
* Mobile frontend integration

---

## 👨‍💻 Developer Notes

This project follows **production ML practices**:

* No notebook-based inference
* Clean environment isolation
* Proper dependency management
* UI + model separation
* Deployment-ready structure

---

## 📄 License

This project is for **educational and research purposes**.

---

## 🏁 Summary

The **Water Quality Prediction System** is a complete ML application that:

* Accepts real-world environmental parameters
* Performs intelligent classification
* Supports batch processing
* Provides a user-friendly interface
* Follows production ML architecture principles

This project demonstrates a full ML pipeline:

> Data → Model → Inference → UI → Deployment

---

**Status:** Production-ready prototype
**Deployment Type:** Streamlit Application
**ML Type:** Supervised Classification
**Domain:** Environmental Intelligence / Water Quality Analytics
