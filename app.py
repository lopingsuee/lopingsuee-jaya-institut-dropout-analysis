import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

from utils.label import (
    select_with_labels,
    COURSE_MAP,
    APPLICATION_MODE_MAP,
    NATIONALITY_MAP,
    MARITAL_STATUS_MAP,
    YES_NO_MAP,
    GENDER_MAP,
    ATTENDANCE_MAP,
)


st.set_page_config(
    page_title="Jaya Institut — Dropout Risk Prediction Prototype",
    layout="wide"
)

@st.cache_resource
def load_model(model_path: str):
    return joblib.load(model_path)

@st.cache_data
def load_reference_data(csv_path: str):
    # Optional: untuk opsi dropdown tambahan jika Anda ingin
    return pd.read_csv(csv_path)


MODEL_PATH = "model/model_fix.joblib"  
DATA_REF_PATH = "data/data_ready_modelling.csv" 


if not Path(MODEL_PATH).exists():
    st.error(f"Model tidak ditemukan di: {MODEL_PATH}")
    st.stop()

model = load_model(MODEL_PATH)

df_ref = None
if Path(DATA_REF_PATH).exists():
    df_ref = load_reference_data(DATA_REF_PATH)


st.title("Jaya Institut — Student Dropout Early Warning Prototype")
st.write(
    "Prototype ini memprediksi **risiko dropout** menggunakan model **Logistic Regression** "
    "berbasis fitur **pendaftaran + performa semester 1**."
)
st.divider()


data = pd.DataFrame()

st.subheader("A. Enrollment & Demographics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    marital_status = select_with_labels(
        "Marital status",
        MARITAL_STATUS_MAP,
        default_value=1,
        key="marital_status",
    )
    data["marital_status"] = [marital_status]

with c2:
    gender = select_with_labels(
        "Gender",
        GENDER_MAP,  # {1:"Male",0:"Female"}
        default_value=0,
        key="gender",
    )
    data["gender"] = [gender]

with c3:
    age_at_enrollment = int(st.number_input("Age at enrollment", value=20, min_value=15, max_value=80))
    data["age_at_enrollment"] = [age_at_enrollment]

with c4:
    international = select_with_labels(
        "International student?",
        YES_NO_MAP,  # {1:"Yes",0:"No"}
        default_value=0,
        key="international",
    )
    data["international"] = [international]

c1, c2, c3, c4 = st.columns(4)

with c1:
    displaced = select_with_labels(
        "Displaced student?",
        YES_NO_MAP,
        default_value=0,
        key="displaced",
    )
    data["displaced"] = [displaced]

with c2:
    educational_special_needs = select_with_labels(
        "Educational special needs?",
        YES_NO_MAP,
        default_value=0,
        key="educational_special_needs",
    )
    data["educational_special_needs"] = [educational_special_needs]

with c3:
    nacionality = select_with_labels(
        "Nationality",
        NATIONALITY_MAP,
        default_value=1,
        key="nacionality",
    )
    data["nacionality"] = [nacionality]

with c4:
    daytime_evening_attendance = select_with_labels(
        "Attendance time",
        ATTENDANCE_MAP,  # {1:"Daytime",0:"Evening"}
        default_value=1,
        key="daytime_evening_attendance",
    )
    data["daytime_evening_attendance"] = [daytime_evening_attendance]

st.subheader("B. Application & Course")

c1, c2, c3, c4 = st.columns(4)

with c1:
    application_mode = select_with_labels(
        "Application mode",
        APPLICATION_MODE_MAP,
        default_value=1,
        key="application_mode",
    )
    data["application_mode"] = [application_mode]

with c2:
    application_order = int(st.number_input("Application order (0–9)", value=0, min_value=0, max_value=9))
    data["application_order"] = [application_order]

with c3:
    course = select_with_labels(
        "Course / Program study",
        COURSE_MAP,
        default_value=list(COURSE_MAP.keys())[0],
        key="course",
    )
    data["course"] = [course]

with c4:
    # course_name dibutuhkan oleh pipeline Anda -> buat otomatis dari course (paling aman)
    course_name = COURSE_MAP.get(course, "Unknown/Other")
    st.text_input("Course name (auto)", value=course_name, disabled=True)
    data["course_name"] = [course_name]

st.subheader("C. Prior Education & Family Background")

c1, c2, c3, c4 = st.columns(4)

with c1:
    # previous_qualification mapping biasanya panjang; kalau Anda sudah buat mapping di utils, pakai itu.
    # Jika belum, biarkan numeric input atau buat mapping menyusul.
    # Di sini saya pakai number_input agar tetap valid untuk model.
    previous_qualification = int(st.number_input("Previous qualification (code)", value=1, min_value=0))
    data["previous_qualification"] = [previous_qualification]

with c2:
    previous_qualification_grade = float(
        st.number_input("Previous qualification grade (0–200)", value=120.0, min_value=0.0, max_value=200.0)
    )
    data["previous_qualification_grade"] = [previous_qualification_grade]

with c3:
    mothers_qualification = int(st.number_input("Mother's qualification (code)", value=1, min_value=0))
    data["mothers_qualification"] = [mothers_qualification]

with c4:
    fathers_qualification = int(st.number_input("Father's qualification (code)", value=1, min_value=0))
    data["fathers_qualification"] = [fathers_qualification]

c1, c2, c3 = st.columns(3)

with c1:
    admission_grade = float(st.number_input("Admission grade (0–200)", value=120.0, min_value=0.0, max_value=200.0))
    data["admission_grade"] = [admission_grade]

with c2:
    mothers_occupation = int(st.number_input("Mother's occupation (code)", value=0, min_value=0))
    data["mothers_occupation"] = [mothers_occupation]

with c3:
    fathers_occupation = int(st.number_input("Father's occupation (code)", value=0, min_value=0))
    data["fathers_occupation"] = [fathers_occupation]

st.subheader("D. Financial Status")

c1, c2, c3 = st.columns(3)

with c1:
    debtor = select_with_labels("Debtor?", YES_NO_MAP, default_value=0, key="debtor")
    data["debtor"] = [debtor]

with c2:
    tuition_fees_up_to_date = select_with_labels(
        "Tuition fees up to date?",
        YES_NO_MAP,
        default_value=1,
        key="tuition_fees_up_to_date",
    )
    data["tuition_fees_up_to_date"] = [tuition_fees_up_to_date]

with c3:
    scholarship_holder = select_with_labels(
        "Scholarship holder?",
        YES_NO_MAP,
        default_value=0,
        key="scholarship_holder",
    )
    data["scholarship_holder"] = [scholarship_holder]

st.subheader("E. Semester 1 Academic Performance")

c1, c2, c3 = st.columns(3)

with c1:
    data["curricular_units_1st_sem_credited"] = [int(st.number_input("1st sem credited", value=0, min_value=0, max_value=60))]
with c2:
    data["curricular_units_1st_sem_enrolled"] = [int(st.number_input("1st sem enrolled", value=6, min_value=0, max_value=60))]
with c3:
    data["curricular_units_1st_sem_evaluations"] = [int(st.number_input("1st sem evaluations", value=6, min_value=0, max_value=60))]

c1, c2, c3 = st.columns(3)

with c1:
    data["curricular_units_1st_sem_approved"] = [int(st.number_input("1st sem approved", value=5, min_value=0, max_value=60))]
with c2:
    data["curricular_units_1st_sem_grade"] = [float(st.number_input("1st sem grade (0–20)", value=12.0, min_value=0.0, max_value=20.0))]
with c3:
    data["curricular_units_1st_sem_without_evaluations"] = [int(st.number_input("1st sem without evaluations", value=0, min_value=0, max_value=60))]

# ----- Section F
st.subheader("F. Macro-Economic Context")

c1, c2, c3 = st.columns(3)

with c1:
    data["unemployment_rate"] = [float(st.number_input("Unemployment rate (%)", value=10.0, min_value=0.0, max_value=100.0))]
with c2:
    data["inflation_rate"] = [float(st.number_input("Inflation rate (%)", value=2.0, min_value=-50.0, max_value=100.0))]
with c3:
    data["gdp"] = [float(st.number_input("GDP", value=0.0))]

st.divider()


col_pred1, col_pred2 = st.columns([1, 2])

with col_pred1:
    threshold = st.slider(
        "Decision threshold (dropout)",
        min_value=0.10,
        max_value=0.90,
        value=0.50,
        step=0.01
    )

predict_btn = st.button("Predict Dropout Risk")

if predict_btn:
    try:
        # Safety check: kolom input harus lengkap sesuai model
        expected_cols = model.named_steps["preprocessor"].feature_names_in_
        missing_cols = set(expected_cols) - set(data.columns)

        if missing_cols:
            st.error(f"Prediction failed: missing columns: {missing_cols}")
            with st.expander("Debug: show expected columns"):
                st.write(list(expected_cols))
            st.stop()

        proba = float(model.predict_proba(data)[:, 1][0])
        pred = 1 if proba >= threshold else 0

        with col_pred2:
            st.subheader("Prediction Result")
            st.write(f"Dropout probability: **{proba:.3f}**")
            st.write(f"Predicted class (threshold={threshold:.2f}): **{pred}**")

            if pred == 1:
                st.error("High Risk: Student is predicted as **Dropout (1)**")
            else:
                st.success("Low Risk: Student is predicted as **Non-Dropout (0)**")

        with st.expander("Show input payload"):
            st.dataframe(data)

    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.write("Pastikan semua kolom input sesuai dengan fitur saat training dan mapping label → code benar.")