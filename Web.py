#python -m streamlit run Web.py

import os
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction ',
                   layout='wide',
                   page_icon="🧑‍⚕️")
diabetes_model=pickle.load(open(r"D:\PythonProject\AICTE_PredictionOfDiseaseOutbreak\Training_model\diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open(r"D:\PythonProject\AICTE_PredictionOfDiseaseOutbreak\Training_model\heart_model.sav",'rb'))
parkinson_model=pickle.load(open(r"D:\PythonProject\AICTE_PredictionOfDiseaseOutbreak\Training_model\perkinson_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Prediction of disease outbreak system',
                         ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Disease Prediction'],
                         menu_icon='hospital-fill', icons=['activity','heart','person'],default_index=0)

if selected== 'Diabetes Prediction':
    st.title("Diabetes prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
       Pregnancies=st.text_input('Number of Pregnancies') 
    with col2:
       Glucose=st.text_input('Glucose level')
    with col3:
       BloodPressure=st.text_input('Blood Pressure value')
    with col1:
       SkinThickness=st.text_input('Skin Thickness value')
    with col2:
       Insulin=st.text_input('Insulin Level')
    with col3:
       BMI=st.text_input('BMI value')
    with col1:
      DiabetesPedigreeFunction =st.text_input('Diabetes Pedigree Function value')
    with col2:
       Age=st.text_input('Age of the person')
    
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'

    st.success(diab_diagnosis)

elif selected=='Heart Disease Prediction':
    st.title("Heart Disease Prediction Using ML")
    col1,col2,col3=st.columns(3)
    with col1:
       age=st.text_input('Age') 
    with col2:
       sex=st.text_input('Sex (0: Female, 1: Male)')
    with col3:
       cp=st.text_input('Chest Pain Type (0-3)')
    with col1:
       trestbps=st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
       chol=st.text_input('Cholestrol level')
    with col3:
       fbs=st.text_input('Fasting Blood Sugar')
    with col1:
      restecg =st.text_input('ECG Results')
    with col2:
       thalach=st.text_input('Max Heart Rate Achieved')
    with col3:
       exang=st.text_input('Exercise-Induced Angina (1: Yes, 0: No)')
    with col1:
       oldpeak=st.text_input('ST Depression')
    with col2:
       slope=st.text_input('ST Slope')
    with col3:
       ca=st.text_input('Major Vessels')
    with col1:
       thal=st.text_input('Thalassemia')
    heart_diagnosis=''
    if st.button('Heart Disease Test Result'):
        user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), 
              float(restecg), float(thalach), float(exang), float(oldpeak),
                float(slope), float(ca), float(thal)]
        user_input=[float(x) for x in user_input]
        heart_prediction=heart_disease_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis='The person has heart disease'
        else:
            heart_diagnosis='The person has no heart disease'

    st.success(heart_diagnosis)


elif selected == "Parkinson Disease Prediction":

    
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)