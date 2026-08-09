import streamlit as st 
st.set_page_config(page_title="Convertisseur" , page_icon="💰", layout="wide")
st.subheader("CONVERTISSEUR")
choix = st.selectbox("Choisissez votre partie à convertir", ["longueur", "poids" , "temperature"])
valeur = st.number_input("entrez la valeur à convertir" , min_value=0, step= 100 )
unite_depart = st.selectbox("choiosisser l'unité de depart",["m","cm","kg","g","°C","°F"])
unite_arrivee = st.selectbox("choisissez l'unité d'arrivée", ["m","cm","kg","g","°C","°F"])
if choix == "longueur":
    if unite_depart == "m" and unite_arrivee == "cm":
        resultat = valeur * 100
    elif unite_depart == "cm" and unite_arrivee == "m":
        resultat = valeur / 1000
    elif unite_depart == unite_arrivee:
        resultat = valeur 
    else:
        st.error("conversion non supportée")
    st.write(f"le résultat est : {resultat} {unite_arrivee}")
elif  choix == "poids":
    if unite_depart == "kg" and unite_arrivee == "g":
            resultat = valeur * 100
    elif unite_depart == "g" and unite_arrivee == "kg":
            resultat = valeur / 1000
    elif unite_depart == unite_arrivee:
            resultat = valeur 
    else:
        st.error("conversion non supportée")
    st.write(f"le résultat est : {resultat} {unite_arrivee}")
elif choix == "temperature":
    if unite_depart == "°C" and unite_arrivee == "°F":
            resultat = (valeur * 9/5) + 32
    elif unite_depart == "°F" and unite_arrivee == "°C":
            resultat = (valeur - 32) * 5/9
    elif unite_depart == unite_arrivee:
            resultat = valeur 
    else:
        st.error("conversion non supportée")
    st.write(f"le résultat est : {resultat} {unite_arrivee}")
     
    
