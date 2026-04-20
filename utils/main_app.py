# main_app.py

import streamlit as st
from utils import preprocessor

st.set_page_config(page_title="🧠 Disease Prediction App", layout="wide")
st.title("🩺 Multi-Disease Prediction Portal")


# Role Selection
role = st.sidebar.selectbox("👤 Select Your Role", ["Doctor", "Analyst", "Admin", "Staff", "Researcher"])

st.markdown(f"### Welcome, **{role}**")

# Show model checkboxes based on the role
st.subheader("🧬 Select the type of Disease Checkup you want to perform:")

# Create a dictionary of model options
model_options = {
    "COVID-19": "Covid_19",
    "RBC Count": "RBC",
    "Urine Infection": "Urine_disease_Prediction",
    "Tumor Detection": "tumor_pred",
    "Kidney Stone": "Kidney_Disease_Prediction",
    "General Health Diseases": "health_diseases"
}

selected_models = []
for label in model_options:
    if st.checkbox(f"✔️ {label}"):
        selected_models.append(label)

# Placeholder for next step (inference UIs)
if selected_models:
    st.markdown("### 🔍 You selected:")
    for selected in selected_models:
        st.write(f"🔹 {selected}")

    st.info("🧠 In the next step, we will load the model UI based on these selections...")

# You can now use this list `selected_models` to route to each model UI (coming next)
