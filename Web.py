#python -m streamlit run Web.py

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Configure the Streamlit page
st.set_page_config(page_title="Prediction of Disease Outbreak",
                   layout='wide',
                   page_icon="doctor")

# Load models
try:
    diabetes_model = pickle.load(open(r"D:\PythonProject\AICTE_Prediction_Practical\Training_model\diabetes_model.sav", "rb"))
    heart_model = pickle.load(open(r"D:\PythonProject\AICTE_Prediction_Practical\Training_model\heart_model.sav", "rb"))
    parkinson_model = pickle.load(open(r"D:\PythonProject\AICTE_Prediction_Practical\Training_model\perkinson_model.sav", "rb"))
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    st.stop()

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title='Prediction of Disease Outbreak System',  # Menu title
        options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Disease Prediction'],  # Options
        icons=['activity', 'heart', 'person'],  # Bootstrap icons
        menu_icon='hospital-fill',  # Menu icon
        default_index=0,  # Default active option
    )

# # Display based on selection
if selected == 'Diabetes Prediction': 
    st.title('Diabetes Prediction using Ml') 
    col1, col2, col3= st.columns(3) 
    with col1: 
        Pregnancies= st.text_input('Number of Pregnancies') 
    with col2: 
        Glucose= st.text_input('Glucose level') 
    with col3: 
        Bloodpressure= st.text_input('Blood Pressure value') 
    with col1: 
        SkinThickness = st.text_input('Skin Thickness value') 
    with col2: 
        Insulin= st.text_input('Insulin level') 
    with col3: 
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of Person')
    # with col3:
    #     if st.button('Predict Diabetes'):

diab_diagnosis= " "
if st.button('Diabetes Test Result'):
    user_input= [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0] == 1:
        diab_diagnosis= "You are Diabetic"
    else:
        diab_diagnosis= 'You are not Diabetic'

st.success(diab_diagnosis)


# Heart Disease Prediction
if selected == 'Heart Disease Prediction': 
    #page title 
    st.title('Heart Disease Prediction using') 
    col1, col2, col3= st.columns(3) 
    with col1: 
        age= st.text_input('Age') 
    with col2: 
        sex= st.text_input('sex') 
    with col3: 
        cp= st.text_input("Chest Pain types") 

    with col1: 
        trestbps= st.text_input('Resting Blood Pressure') 
    with col2: 
        chol= st.text_input('Serum Cholestoral in ag/dl') 
    with col3: 
        fbs= st.text_input('Fasting Blood Sugar 120 mg/dl') 

    with col1: 
        restecg= st.text_input('Besting Electrocardiographic results') 
    with col2: 
        thalach= st.text_input('Maximun Heart Rate achieved') 
    with col3: 
        exang= st.text_input('Exercise Induced Angina') 
    
    with col1: 
        oldpeak= st.text_input('ST depression induced by exercise') 
    with col2: 
        slope= st.text_input('Slope of the peak exercise ST segment')
    with col3: 
        ca= st.text_input('Major vessels colored by flourosopy') 
    
    with col1: 
        thal= st.text_input('thal: normal; 1 fixed defect; 2 reversable defect') 

    #code for Prediction 
    heart_diagnosis= ''
    #creating a button for Prediction 
    if st.button('Heart Disease Test Result'): 
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal] 
        user_input = [float(x) for x in user_input] 
        heart_prediction= heart_model.predict([user_input]) 

        if heart_prediction[0] == 1: 
            heart_diagnosis= 'The person is having heart disease' 
        else: 
            heart_diagnosis= 'The person does not have any heart disease' 
    st.success(heart_diagnosis)



if selected == 'Parkinson Disease Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input('Name')
    with col2:    
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
    with col3:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
    with col1:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col2:
        NHR = st.text_input('NHR')
    with col3:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col1:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col3:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')
    

    perkinson_diagnosis= " "
    if st.button("Parkinson's Test Result"):
        user_input = [float(x) for x in [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
        parkinson_prediction = parkinson_model.predict([user_input])

        if parkinson_prediction[0] == 1: 
            parkinson_prediction= 'The person is having Perkinsons disease' 
        else: 
            parkinson_prediction= 'The person does not have any Perkinsons disease' 
    st.success(perkinson_diagnosis)
