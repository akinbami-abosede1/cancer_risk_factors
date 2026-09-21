import streamlit as st
import pandas as pd
import joblib


# 1. PAGE CONFIGURATION


st.set_page_config(
    page_title="Cancer Risk Prediction",
    page_icon="🩺",
    layout="centered"
)



# 2. LOAD THE TRAINED MODEL


model = joblib.load("cancer_risk_model.pkl")



# 3. CUSTOM CSS


st.markdown("""
<style>

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 27px;
        font-weight: 650;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    /* About section */
    .about-text {
        width: 100%;
        object-fit: contain;
        text-align: justify;
    }

    /* Prediction result */
    .prediction-title {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-top: 25px;
    }

    /* Center prediction button */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    div.stButton > button {
        width: 280px;
        height: 55px;
        font-size: 18px;
        font-weight: 700;
    }

    /* Disclaimer */
    .disclaimer {
        font-size: 15px;
        line-height: 1.7;
    }

</style>
""", unsafe_allow_html=True)



# 4. MAIN TITLE


st.markdown(
    '<div class="main-title">Cancer Risk Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning-Based Cancer Risk Prediction'
    '</div>',
    unsafe_allow_html=True
)



# 5. ABOUT THE APP


about_image, about_text = st.columns([1.05, 1])

with about_image:
   st.image(
           "_.jpeg",
           width=400
    )

with about_text:

    st.markdown(
        '<div class="section-title">About the App</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="about-text">
    This application is a machine learning-based tool designed to
    estimate an individual's cancer risk level using selected
    demographic, lifestyle, environmental, medical and genetic factors.
    
    The model provides an estimated risk level of
    <b>Low, Medium, or High</b> based on the information provided.
    </div>
    """, unsafe_allow_html=True)

    st.write("Click the link below to learn more about cancer and Factors associated with it.")

    st.link_button(
        "Learn More About Cancer Risk",
        "https://www.who.int/health-topics/cancer"
    )


# 6. PREDICTION SECTION


st.markdown("---")

st.markdown(
    '<div class="main-title">Predict Your Cancer Risk</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter the information below to receive an estimated cancer risk level.'
    '</div>',
    unsafe_allow_html=True
)



# 7. PERSONAL INFORMATION


st.markdown(
    '<div class="section-title">Personal Information</div>',
    unsafe_allow_html=True
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=200,
    value=40,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=70.0,
    value=25.0,
    step=0.1
)



# 8. BMI CATEGORY


if bmi < 18.5:
    bmi_category = "Underweight"

elif bmi < 25:
    bmi_category = "Normal weight"

elif bmi < 30:
    bmi_category = "Overweight"

else:
    bmi_category = "Obese"


st.info(f"**BMI Category:** {bmi_category}")



# 9. CANCER INFORMATION


st.markdown(
    '<div class="section-title">Cancer Information</div>',
    unsafe_allow_html=True
)

cancer_type = st.selectbox(
    "Select Cancer Type",
    ["Breast", "Colon", "Lung", "Prostate", "Skin"]
)



# 10. LIFESTYLE FACTORS


st.markdown(
    '<div class="section-title">Lifestyle Factors</div>',
    unsafe_allow_html=True
)

smoking = st.slider(
    "Smoking",
    min_value=1,
    max_value=10,
    value=5
)

alcohol_use = st.slider(
    "Alcohol Use",
    min_value=1,
    max_value=10,
    value=5
)

obesity = st.slider(
    "Obesity",
    min_value=1,
    max_value=10,
    value=5
)

diet_red_meat = st.slider(
    "Red Meat Consumption",
    min_value=1,
    max_value=10,
    value=5
)

diet_salted_processed = st.slider(
    "Salted/Processed Food Consumption",
    min_value=1,
    max_value=10,
    value=5
)

fruit_veg_intake = st.slider(
    "Fruit and Vegetable Intake",
    min_value=1,
    max_value=10,
    value=5
)

physical_activity = st.slider(
    "Physical Activity",
    min_value=1,
    max_value=10,
    value=5
)



# 11. ENVIRONMENTAL FACTORS


st.markdown(
    '<div class="section-title">Environmental Factors</div>',
    unsafe_allow_html=True
)

air_pollution = st.slider(
    "Air Pollution Exposure",
    min_value=1,
    max_value=10,
    value=5
)

occupational_hazards = st.slider(
    "Occupational Hazards",
    min_value=1,
    max_value=10,
    value=5
)



# 12. MEDICAL AND GENETIC FACTORS


st.markdown(
    '<div class="section-title">Medical & Genetic Factors</div>',
    unsafe_allow_html=True
)

family_history = st.selectbox(
    "Family History of Cancer",
    ["Yes", "No"]
)

brca_mutation = st.selectbox(
    "Breast Cancer Gene(BRCA) Mutation",
    ["Yes", "No"]
)

h_pylori = st.selectbox(
    "H. Pylori Infection (Stomach Bacteria)",
    ["Yes", "No"]
)

calcium_intake = st.slider(
    "Calcium Intake",
    min_value=1,
    max_value=10,
    value=5
)



# 13. CONVERT CATEGORICAL VARIABLES


gender_value = 1 if gender == "Male" else 0

family_history_value = 1 if family_history == "Yes" else 0

brca_value = 1 if brca_mutation == "Yes" else 0

h_pylori_value = 1 if h_pylori == "Yes" else 0



# 14. CREATE CANCER TYPE DUMMY VARIABLES


cancer_dummies = {
    "Cancer_Type_Breast": 0,
    "Cancer_Type_Colon": 0,
    "Cancer_Type_Lung": 0,
    "Cancer_Type_Prostate": 0,
    "Cancer_Type_Skin": 0
}

cancer_dummies[f"Cancer_Type_{cancer_type}"] = 1



# 15. CREATE INPUT DATAFRAME


input_data = pd.DataFrame([{

    "Age": age,
    "Gender": gender_value,
    "Smoking": smoking,
    "Alcohol_Use": alcohol_use,
    "Obesity": obesity,
    "Family_History": family_history_value,
    "Diet_Red_Meat": diet_red_meat,
    "Diet_Salted_Processed": diet_salted_processed,
    "Fruit_Veg_Intake": fruit_veg_intake,
    "Physical_Activity": physical_activity,
    "Air_Pollution": air_pollution,
    "Occupational_Hazards": occupational_hazards,
    "BRCA_Mutation": brca_value,
    "H_Pylori_Infection": h_pylori_value,
    "Calcium_Intake": calcium_intake,
    "BMI": bmi,
    **cancer_dummies

}])



# 16. ENSURE CORRECT FEATURE ORDER


feature_columns = [

    "Age","Gender","Smoking","Alcohol_Use","Obesity","Family_History",

    "Diet_Red_Meat","Diet_Salted_Processed", "Fruit_Veg_Intake", "Physical_Activity",

    "Air_Pollution","Occupational_Hazards","BRCA_Mutation","H_Pylori_Infection",

    "Calcium_Intake","BMI","Cancer_Type_Breast","Cancer_Type_Colon","Cancer_Type_Lung",

    "Cancer_Type_Prostate","Cancer_Type_Skin"

]

input_data = input_data[feature_columns]



# 17. PREDICTION BUTTON


col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    predict_button = st.button(
        "Predict Cancer Risk",
        use_container_width=True
    )



# 18. MAKE PREDICTION


if predict_button:

    prediction = model.predict(input_data)[0]

    risk_levels = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }

    risk_result = risk_levels[prediction]


   
    # Prediction Result
   

    st.markdown(
        '<div class="prediction-title">Prediction Result</div>',
        unsafe_allow_html=True
    )


    if prediction == 0:

        st.success(
            f"### Predicted Risk Level: {risk_result}"
        )

    elif prediction == 1:

        st.warning(
            f"### Predicted Risk Level: {risk_result}"
        )

    else:

        st.error(
            f"### Predicted Risk Level: {risk_result}"
        )


    st.write(
        "This result represents the risk level predicted by the "
        "machine learning model based on the information provided."
    )



# 19. DISCLAIMER


st.markdown("---")

st.markdown(
    '<div class="section-title">Disclaimer</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="disclaimer">

This application is intended for <b>educational and research purposes only</b>.
The risk level generated by this application is an estimate produced by a
machine learning model based on the information provided by the user.

The prediction is <b>not a medical diagnosis</b> and should not be used as
a substitute for professional medical advice, diagnosis, or treatment.
The model may not account for all factors that influence an individual's
cancer risk.

If you have health concerns or believe you may be at risk of cancer,
please consult a qualified healthcare professional for appropriate
medical evaluation and advice.

</div>
""", unsafe_allow_html=True)
