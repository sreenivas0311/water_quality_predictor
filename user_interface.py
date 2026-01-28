import streamlit as st
import pickle
import pandas as pd
import numpy as np

@st.cache_resource
def load_assets():
    with open("water_quality_xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("feature_columns.pkl", "rb") as f:
        feature_columns = pickle.load(f)
    with open("label_mapping.pkl", "rb") as f:
        label_mapping = pickle.load(f)
    return model, feature_columns, label_mapping


UNITS = {
    "Approx Depth": "m","Temperature": "°C","Dissolved O2": "mg/L","pH": "pH",
    "Conductivity": "µS/cm","BOD": "mg/L","Nitrate N": "mg/L",
    "Fecal Coliform": "MPN/100mL","Total Coliform": "MPN/100mL",
    "Fecal Streptococci": "MPN/100mL","Turbidity": "NTU",
    "Phenophelene Alkanity": "mg/L","Total Alkalinity": "mg/L",
    "Chlorides": "mg/L","COD": "mg/L","Total Kjeldahl N": "mg/L",
    "Amonia N": "mg/L","Hardness CaCo3": "mg/L","Calcium CaCo3": "mg/L",
    "Magnesium CaCo3": "mg/L","Sulphate": "mg/L","Sodium": "mg/L",
    "Total Dissolved Solids": "mg/L","Total Fixed Solids": "mg/L",
    "Total Suspended Solids": "mg/L","Phosphate": "mg/L","Boron": "mg/L",
    "Potassium": "mg/L","Flouride": "mg/L"
}


def render_ui():

    model, feature_columns, label_mapping = load_assets()

    if "mode" not in st.session_state:
        st.session_state.mode = "user"

    # ---------- SIDEBAR ----------
    st.sidebar.markdown("## 💧 Water Quality System")
    st.sidebar.markdown("---")

    if st.sidebar.button("User Entry Mode"):
        st.session_state.mode = "user"

    if st.sidebar.button("Excel File Mode"):
        st.session_state.mode = "excel"

    uploaded_file = None
    if st.session_state.mode == "excel":
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Excel Upload")
        uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xls", "xlsx"])

    # ---------- CAUTION ----------
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        ⚠️ **Caution**  
        This model is trained on a limited dataset.  
        Predictions are statistical, not scientific rules.  
        Extreme values in a single feature may not dominate predictions.  

        **Decision-support system only.**
        """
    )

    # ---------- MAIN ----------
    st.markdown("# Water Quality Prediction System")
    st.caption("Machine Learning based Water Quality Classification")

    # ---------- USER MODE ----------
    if st.session_state.mode == "user":

        st.subheader("Manual Data Entry")

        inputs = {}
        cols = st.columns(3)
        i = 0

        for feature in feature_columns:
            unit = UNITS.get(feature, "")
            with cols[i]:
                inputs[feature] = st.number_input(
                    f"{feature} ({unit})",
                    value=0.0,
                    step=0.1
                )
            i = (i + 1) % 3

        if st.button("Predict Water Quality"):
            data = np.array([inputs[f] for f in feature_columns]).reshape(1, -1)
            pred = model.predict(data)[0]
            label = label_mapping.get(pred, pred)

            st.success(f"🧪 Prediction Result: {label}")

    # ---------- EXCEL MODE ----------
    else:
        st.subheader("Excel File Prediction")

        if uploaded_file:
            df = pd.read_excel(uploaded_file)

            missing = [c for c in feature_columns if c not in df.columns]
            if missing:
                st.error("Missing required columns:")
                st.write(missing)
            else:
                preds = model.predict(df[feature_columns].values)
                labels = [label_mapping.get(p, p) for p in preds]

                df_out = df.copy()
                df_out["Prediction"] = labels

                st.dataframe(df_out, use_container_width=True)

                csv = df_out.to_csv(index=False).encode("utf-8")
                st.download_button("Download Results", csv, "water_quality_results.csv", "text/csv")
        else:
            st.info("Upload Excel file from the left panel.")
