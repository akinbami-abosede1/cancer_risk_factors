# Cancer Risk Analysis and Prediction

## Project Overview

This project analyzes factors associated with cancer risk and develops a machine learning model for predicting cancer risk levels based on demographic, lifestyle, genetic, environmental, and health-related factors.

The project combines **data analysis, machine learning, and interactive data visualization**. The analysis was performed in Python using a Jupyter Notebook, while a Streamlit application was developed to allow users to explore the cancer risk data interactively as well as predicting cancer risk level.

The project covers different cancer types, including:

* Breast Cancer
* Colon Cancer
* Lung Cancer
* Prostate Cancer
* Skin Cancer

The analysis focuses on understanding patterns in the dataset and identifying factors that are associated with differences in overall cancer risk.

---

## Project Objectives

The main objectives of this project are to:

* Examine demographic and health-related characteristics of the dataset.
* Investigate lifestyle, genetic, environmental, and other factors associated with cancer risk.
* Build a machine learning model for cancer risk prediction.
* Present the results through an interactive Streamlit dashboard.

---

## Dataset

The dataset used in this project contains information relating to cancer risk factors and cancer types.

### Main Variables

The dataset includes variables covering areas such as:

* Cancer type
* Age group
* Lifestyle factors
* Dietary factors
* Genetic factors
* Environmental factors
* BMI category
* Risk level

The dataset is contained in:

```text
cancer_risk.csv
```

### Cancer Types

The analysis covers the following cancer types:

* Breast
* Colon
* Lung
* Prostate
* Skin

---

## Tools and Technologies

The following tools and technologies were used:

| Tool             | Purpose                                    |
| ---------------- | ------------------------------------------ |
| Python           | Data analysis and machine learning         |
| Pandas           | Data manipulation and preprocessing        |
| NumPy            | Numerical operations                       |
| Matplotlib       | Data visualization                         |
| Seaborn          | Statistical visualization                  |
| Scikit-learn     | Machine learning                           |
| Jupyter Notebook | Exploratory analysis and model development |
| Streamlit        | Interactive dashboard                      |
| Git & GitHub     | Version control and project sharing        |

---

## Project Structure

```text
cancer-risk-analysis/
│
├── cancer_risk_factor.ipynb
├── app.py
├── cancer_risk.csv
└── README.md
```

### File Description

**`cancer_risk_factor.ipynb`**

Contains the main data analysis and machine learning workflow, including data exploration, preprocessing, visualization, and model development.

**`app.py`**

Contains the Streamlit application for model deployment. It provides an interface where users can input relevant cancer risk factors and receive a predicted cancer risk level from the trained machine learning model.

**`dashboard.py`**

Contains the Streamlit application for interactive data visualization. It allows users to explore cancer risk patterns in the dataset using filters, charts, and summary visualizations across different cancer types and risk factors.

**`cancer_risk.csv`**

The dataset used for the analysis and Streamlit dashboard.

**`README.md`**

Provides documentation for the project.


# Data Analysis Workflow

## 1. Data Loading

The dataset was imported into Python using Pandas.

---

## 2. Data Preprocessing

The dataset was prepared before performing exploratory analysis and machine learning.

The preprocessing stage included:

* Checking for missing values
* Checking for duplicate observations
* Examining data types
* Preparing categorical variables
* Preparing the data for machine learning

---

## 3. Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to identify patterns within the dataset.

The analysis examined:

### Cancer Type Distribution

The distribution of observations across the different cancer types was examined to understand how the dataset is represented across cancer categories.

### Age Group

Age groups were analyzed to examine how cancer cases and risk levels vary across different age categories.

### Lifestyle Factors

Lifestyle-related variables were explored to understand their relationship with cancer risk.

These include factors related to:

* Physical activity
* Smoking
* Alcohol consumption


### Dietary Factors

Diet-related variables were analyzed to examine their association with cancer risk.

### Genetic Factors

Genetic and family-related variables were examined as potential contributors to cancer risk.

### Environmental Factors

Environmental variables were explored to identify patterns that may be associated with differences in cancer risk.

---

# Machine Learning

A machine learning component was included to predict cancer risk based on the available risk factors.

The modelling workflow involved:

1. Selecting relevant features.
2. Separating predictor variables from the target variable.
3. Preparing categorical and numerical variables.
4. Splitting the data into training and testing sets.
5. Training the machine learning model.
6. Generating predictions.
7. Evaluating model performance.


> **Important:** The model is intended for educational and analytical purposes. It is not a clinical diagnostic tool and should not be used to make medical decisions.

---

# The project includes two Streamlit applications

### app.py – Model Deployment
Provides an interactive interface for users to enter cancer risk factors and receive a predicted risk level from the trained machine learning model.

### dashboard.py – Data Visualization
Provides an interactive dashboard for exploring the cancer risk dataset through visualizations and filters based on cancer type and risk factors.

---

# Key Findings

* Higher-risk observations generally recorded higher scores for several lifestyle, dietary, and environmental factors.
* Smoking was particularly prominent in the lung cancer results, while obesity and alcohol use were more prominent in the breast cancer results.
* Red-meat consumption and salted/processed-food consumption recorded relatively high scores in the colon and prostate cancer results.
Air pollution was particularly prominent in the lung and colon cancer results, while occupational hazards were notable in the skin cancer results.
The patterns varied across cancer types, showing that different risk-factor scores were more prominent within different cancer categories.
* Air pollution was particularly prominent in the lung and colon cancer results, while occupational hazards were notable in the skin cancer results.
* The patterns varied across cancer types, showing that different risk-factor scores were more prominent within different cancer categories.

---

# Running the Project

## 1. Clone the Repository

Clone this repository to your local computer using Git:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project directory:

```bash
cd cancer-risk-analysis
```

## 2. Install Dependencies

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit jupyter
```

## 3. Run the Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
cancer_risk_factor.ipynb
```

and run the cells sequentially.

## 4. Run the Streamlit Application

Start the dashboard with:

```bash
streamlit run dashboard.py
```

Start the application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# Limitations

This project has some limitations that should be considered when interpreting the results.

* The analysis is based on the available dataset and its variables.
* Associations observed in the data do not necessarily imply causation.
* The dataset may not represent the broader population.
* Machine learning predictions depend on the quality and characteristics of the training data.
* The model should not be interpreted as a medical diagnostic system.

---

# Future Improvements

Future development of the project could include:

* Testing additional machine learning algorithms.
* Hyperparameter tuning and cross-validation.
* Improving model evaluation.
* Expanding the dataset with additional observations and clinically relevant variables.
* Deploying the Streamlit application online.

---

# Disclaimer

This project is intended for **educational, analytical, and portfolio purposes only**. The predictions generated by the model should not be considered medical advice, diagnosis, or clinical recommendations.

---

# Author

**Abosede Akinbami**

Data Analyst

### Skills Demonstrated

* Python
* SQL
* Excel
* Power BI
* SPSS
* Data Analysis
* Data Visualization
* Machine Learning

### Connect

* GitHub: `https://github.com/akinbami-abosede1`
* LinkedIn: `https://www.linkedin.com/in/akinbami-abosede`
