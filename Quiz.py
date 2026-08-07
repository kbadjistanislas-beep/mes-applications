import streamlit as st

score = 0

with st.form("quiz_form"):
    v1 = st.radio("Q1: Capitale de la France ?" , ["Paris","Marseille","Lyon"])
    v2 = st.radio("Q2: 8 + 5 = ?" , ["10","52","13"])
    v3 = st.radio("Q3: Language utilisé avec Streamlit", ["Python","java","C++"])
    v4 = st.radio("Q4: Capitale du canada", ["Toronto","Ottawa","Montréal"])
    v5 = st.radio("Q5: Mot-clé pour créer une fonction en Python ? ", ["func","def","fct"])

    valider = st.form_submit_button("valider")

if valider:
    if v1 == "Paris":
        score += 1
    if v2 == "13":
        score += 1
    if v3 == "Python":
        score += 1
    if v4 == "Ottawa":
        score += 1
    if v5 == "def":
        score += 1
        
