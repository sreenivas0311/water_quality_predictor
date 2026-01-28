import streamlit as st
from user_interface import render_ui

st.set_page_config(
    page_title="Water Quality Prediction System",
    page_icon="💧",
    layout="wide"
)

st.markdown("""
<style>

/* ================= SIDEBAR ================= */
section[data-testid="stSidebar"] {
    background-color: #000000;
}
section[data-testid="stSidebar"] * {
    color: white;
}

/* ================= MAIN AREA ================= */
section[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
    padding: 25px;
}

/* ================= BUTTONS ================= */
.stButton > button {
    background-color: #000000 !important;
    color: #ffffff !important;
    border: 1px solid #ffffff !important;
    width: 100%;
    border-radius: 6px;
    padding: 6px 10px !important;
}

/* No hover / no effects */
.stButton > button:hover,
.stButton > button:focus,
.stButton > button:active {
    background-color: #000000 !important;
    color: #ffffff !important;
    border: 1px solid #ffffff !important;
    box-shadow: none !important;
    outline: none !important;
}

/* ================= FILE UPLOADER ================= */

/* Outer uploader box */
[data-testid="stFileUploader"] {
    background-color: #000000 !important;
    border: 1px solid #ffffff !important;
    border-radius: 6px;
    padding: 6px !important;
    margin: 4px 0 !important;
}

/* Dropzone */
[data-testid="stFileUploaderDropzone"] {
    background-color: #000000 !important;
    border: 1px solid #ffffff !important;
    padding: 6px !important;
    margin: 0 !important;
}

/* Inner container */
[data-testid="stFileUploaderDropzone"] > div {
    padding: 4px !important;
    margin: 0 !important;
}

/* Section */
[data-testid="stFileUploaderDropzone"] section {
    padding: 4px !important;
    margin: 0 !important;
    min-height: unset !important;
}

/* Text spacing */
[data-testid="stFileUploaderDropzone"] p,
[data-testid="stFileUploaderDropzone"] span {
    margin: 2px 0 !important;
    padding: 0 !important;
    color: #ffffff !important;
}

/* Browse button */
[data-testid="stFileUploaderDropzone"] button {
    background-color: #000000 !important;
    color: #ffffff !important;
    border: 1px solid #ffffff !important;
    padding: 4px 8px !important;
    margin-top: 4px !important;
}

/* Disable hover on browse */
[data-testid="stFileUploaderDropzone"] button:hover {
    background-color: #000000 !important;
    color: #ffffff !important;
    border: 1px solid #ffffff !important;
}

/* ================= GLOBAL SPACING ================= */
.block-container {
    padding-top: 8px !important;
    padding-bottom: 8px !important;
}

.element-container {
    margin-bottom: 4px !important;
}

/* Sidebar spacing */
section[data-testid="stSidebar"] .element-container {
    margin-bottom: 6px !important;
}

</style>
""", unsafe_allow_html=True)



render_ui()
