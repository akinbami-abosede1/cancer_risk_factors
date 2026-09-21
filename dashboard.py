# CANCER RISK FACTORS DASHBOARD
# Streamlit Application

import streamlit as st
import pandas as pd
import plotly.express as px
import os


# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="Cancer Risk Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 2. CUSTOM CSS

st.markdown("""
<style>

    /* Main page */
    .stApp {
        background-color: #ffffff;
    }

    /* Reduce top spacing */
    .block-container {
        padding-top: 5rem;
        padding-bottom: 2rem;
    }

    /* Main title */
    .main-title {
        text-align: center;
        color: #1565C0;
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 15px;
        margin-bottom: 20px;
    }

    /* Section titles */
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #1565C0;
        border-bottom: 2px solid #1565C0;
        padding-bottom: 5px;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    /* KPI cards */
    .metric-card {
        background-color: #EAF4FF;
        border-left: 4px solid #1976D2;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        min-height: 105px;
    }

    .metric-title {
        font-size: 14px;
        color: #555555;
        font-weight: 600;
    }

    .metric-value {
        font-size: 30px;
        color: #1565C0;
        font-weight: 700;
        margin-top: 5px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #EAF4FF;
        margin-top: 60px;
    }

    .sidebar-title {
        text-align: center;
        background-color: #1976D2;
        color: white;
        padding: 8px;
        border-radius: 8px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* Sidebar image */
    .sidebar-image {
        border-radius: 8px;
        margin-bottom: 15px;
    }

  /* Cancer type radio button text */
    [data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {
        color: #1565C0 !important;
        font-weight: 600 !important;
    }

    /* Chart containers */
    .chart-container {
        border: 1px solid #D6E4F0;
        border-radius: 8px;
        padding: 5px;
        background-color: white;
    }

</style>
""", unsafe_allow_html=True)


# 3. LOAD DATA

@st.cache_data
def load_data():

    df = pd.read_csv("cancer_risk.csv")

  
  
    # Convert Yes/No columns to numeric values
    # Yes = 1
    # No  = 0
  
  

    binary_columns = [
        "Family_History",
        "BRCA_Mutation",
        "H_Pylori_Infection"
    ]

    for col in binary_columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .map({
                "Yes": 1,
                "No": 0
            })
        )

  
  
    # Make sure numerical columns are numeric
  
  

    numeric_columns = [
        "Age",
        "Smoking",
        "Alcohol_Use",
        "Obesity",
        "Diet_Red_Meat",
        "Diet_Salted_Processed",
        "Fruit_Veg_Intake",
        "Physical_Activity",
        "Air_Pollution",
        "Occupational_Hazards",
        "Calcium_Intake",
        "BMI",
        "Physical_Activity_Level",
        "Overall_Risk_Score"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


df = load_data()


# 4. CHECK REQUIRED COLUMNS

required_columns = [
    "Cancer_Type",
    "Age",
    "Age_group",
    "Gender",
    "Smoking",
    "Alcohol_Use",
    "Obesity",
    "Family_History",
    "Diet_Red_Meat",
    "Diet_Salted_Processed",
    "Fruit_Veg_Intake",
    "Physical_Activity",
    "Air_Pollution",
    "Occupational_Hazards",
    "BRCA_Mutation",
    "H_Pylori_Infection",
    "Calcium_Intake",
    "BMI",
    "BMI category",
    "Physical_Activity_Level",
    "Overall_Risk_Score",
    "Risk_Level"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    st.error(
        "The following columns are missing from the dataset:\n\n"
        + ", ".join(missing_columns)
    )
    st.stop()


# 5. SIDEBAR

with st.sidebar:


    st.markdown(
        '<div class="sidebar-title">CANCER RISK ANALYSIS</div>',
        unsafe_allow_html=True
    )

    # Put your image in the same folder as app.py
    # and name it cancer_image.png

    image_path = "_.jpeg"

    if os.path.exists(image_path):
        st.image(
            image_path,
            use_container_width=True
        )
    else:
        st.info(
            "Add your cancer image as "
            "`cancer_image.png` in the same folder as app.py."
        )

  
  
    # Cancer Type Filter
  
  

    st.markdown(
        '<div class="sidebar-title">CANCER TYPE</div>',
        unsafe_allow_html=True
    )

    cancer_types = sorted(
        df["Cancer_Type"].dropna().unique().tolist()
    )

    selected_cancer = st.radio(
        "Select Cancer Type",
        ["All Cancer Types"] + cancer_types,
        index=0
    )


# 6. FILTER DATA

if selected_cancer == "All Cancer Types":

    filtered_df = df.copy()
    dashboard_title = "All Cancer Types"

else:

    filtered_df = df[
        df["Cancer_Type"] == selected_cancer
    ].copy()

    dashboard_title = selected_cancer


# 7. MAIN TITLE

st.markdown(
    '<div class="main-title">'
    'VISUALIZATION OF RISK FACTORS ASSOCIATED WITH CANCER'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">'
    f'Currently viewing: <b>{dashboard_title}</b>'
    f'</div>',
    unsafe_allow_html=True
)


# 8. KPI CARDS

total_patients = len(filtered_df)

number_cancer_types = filtered_df[
    "Cancer_Type"
].nunique()

average_bmi = filtered_df[
    "BMI"
].mean()

high_risk = (
    filtered_df["Risk_Level"]
    .astype(str)
    .str.lower()
    .eq("high")
    .sum()
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Total Patients</div>
            <div class="metric-value">{total_patients:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Cancer Types</div>
            <div class="metric-value">{number_cancer_types}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Average BMI</div>
            <div class="metric-value">{average_bmi:.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">High Risk Patients</div>
            <div class="metric-value">{high_risk:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# 9. DEMOGRAPHIC FACTORS

st.markdown(
    '<div class="section-title">DEMOGRAPHIC FACTORS</div>',
    unsafe_allow_html=True
)

demo_col1, demo_col2, demo_col3 = st.columns(3)



# Age Distribution


with demo_col1:

    fig_age = px.histogram(
        filtered_df,
        x="Age",
        nbins=15,
        title="Distribution of Age",
        labels={
            "Age": "Age"
        },
        template="plotly_white"
    )

    fig_age.update_layout(
        height=300,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )



# Age Group


with demo_col2:

    age_group_count = (
        filtered_df["Age_group"]
        .value_counts()
        .reset_index()
    )

    age_group_count.columns = [
        "Age_group",
        "Count"
    ]

    fig_age_group = px.bar(
        age_group_count,
        x="Age_group",
        y="Count",
        title="Distribution of Age Group",
        labels={
            "Age_group": "Age Group",
            "Count": "Number of Patients"
        },
        template="plotly_white"
    )

    fig_age_group.update_layout(
        height=300,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    st.plotly_chart(
        fig_age_group,
        use_container_width=True
    )



# Gender


with demo_col3:

    gender_count = (
        filtered_df["Gender"]
        .value_counts()
        .reset_index()
    )

    gender_count.columns = [
        "Gender",
        "Count"
    ]

    fig_gender = px.pie(
        gender_count,
        names="Gender",
        values="Count",
        hole=0.55,
        title="Distribution of Gender"
    )

    fig_gender.update_layout(
        height=300,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    st.plotly_chart(
        fig_gender,
        use_container_width=True
    )


# 10. LIFESTYLE + DIETARY FACTORS

life_col, diet_col = st.columns(2)


# 10A. LIFESTYLE FACTORS

with life_col:

    st.markdown(
        '<div class="section-title">'
        'LIFESTYLE FACTORS'
        '</div>',
        unsafe_allow_html=True
    )

    lifestyle_columns = [
        "Smoking",
        "Physical_Activity",
        "Alcohol_Use",
        "Obesity"
    ]

    lifestyle_data = (
        filtered_df
        .groupby("Risk_Level")[lifestyle_columns]
        .mean()
        .reset_index()
    )

    lifestyle_long = lifestyle_data.melt(
        id_vars="Risk_Level",
        var_name="Factor",
        value_name="Average Score"
    )

    fig_lifestyle = px.bar(
        lifestyle_long,
        x="Risk_Level",
        y="Average Score",
        color="Factor",
        barmode="group",
        title="Lifestyle Factors by Risk Level",
        template="plotly_white"
    )

    fig_lifestyle.update_layout(
        height=360,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        legend_title_text=""
    )

    st.plotly_chart(
        fig_lifestyle,
        use_container_width=True
    )


# 10B. DIETARY FACTORS

with diet_col:

    st.markdown(
        '<div class="section-title">'
        'DIETARY FACTORS'
        '</div>',
        unsafe_allow_html=True
    )

    dietary_columns = [
        "Fruit_Veg_Intake",
        "Diet_Salted_Processed",
        "Diet_Red_Meat",
        "Calcium_Intake"
    ]

    dietary_data = (
        filtered_df
        .groupby("Risk_Level")[dietary_columns]
        .mean()
        .reset_index()
    )

    dietary_long = dietary_data.melt(
        id_vars="Risk_Level",
        var_name="Factor",
        value_name="Average Score"
    )

    fig_dietary = px.bar(
        dietary_long,
        x="Risk_Level",
        y="Average Score",
        color="Factor",
        barmode="group",
        title="Dietary Factors by Risk Level",
        template="plotly_white"
    )

    fig_dietary.update_layout(
        height=360,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        legend_title_text=""
    )

    st.plotly_chart(
        fig_dietary,
        use_container_width=True
    )


# 11. HEALTH & GENETIC + ENVIRONMENTAL FACTORS

health_col, environment_col = st.columns(2)


# 11A. HEALTH & GENETIC FACTORS

with health_col:

    st.markdown(
        '<div class="section-title">'
        'HEALTH & GENETIC FACTORS'
        '</div>',
        unsafe_allow_html=True
    )

    health_columns = [
        "BRCA_Mutation",
        "H_Pylori_Infection",
        "Family_History"
    ]

    health_data = (
        filtered_df
        .groupby("Risk_Level")[health_columns]
        .mean()
        .reset_index()
    )

    health_long = health_data.melt(
        id_vars="Risk_Level",
        var_name="Factor",
        value_name="Average Score"
    )

    fig_health = px.bar(
        health_long,
        x="Risk_Level",
        y="Average Score",
        color="Factor",
        barmode="group",
        title="Health & Genetic Factors by Risk Level",
        template="plotly_white"
    )

    fig_health.update_layout(
        height=360,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        legend_title_text=""
    )

    st.plotly_chart(
        fig_health,
        use_container_width=True
    )


# 11B. ENVIRONMENTAL & OCCUPATIONAL FACTORS

with environment_col:

    st.markdown(
        '<div class="section-title">'
        'ENVIRONMENTAL & OCCUPATIONAL FACTORS'
        '</div>',
        unsafe_allow_html=True
    )

    environmental_columns = [
        "Air_Pollution",
        "Occupational_Hazards"
    ]

    environmental_data = (
        filtered_df
        .groupby("Risk_Level")[environmental_columns]
        .mean()
        .reset_index()
    )

    environmental_long = environmental_data.melt(
        id_vars="Risk_Level",
        var_name="Factor",
        value_name="Average Score"
    )

    fig_environment = px.bar(
        environmental_long,
        x="Risk_Level",
        y="Average Score",
        color="Factor",
        barmode="group",
        title="Environmental & Occupational Factors by Risk Level",
        template="plotly_white"
    )

    fig_environment.update_layout(
        height=360,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        legend_title_text=""
    )

    st.plotly_chart(
        fig_environment,
        use_container_width=True
    )




# 13. FOOTER

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center; color:#777; font-size:13px;">
        Cancer Risk Factors Visualization Dashboard
    </div>
    """,
    unsafe_allow_html=True
)