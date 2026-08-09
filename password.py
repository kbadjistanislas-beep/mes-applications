import streamlit as st
import string, secrets
longueur = st.slider("Longueur" , 6, 32, 12)
caracteres = string.ascii_letters
if st.checkbox("Inclure des chiffres"):
    caracteres += string.digits
if st.checkbox("Inclure des symboles"):
    caracteres += string.punctuation
password = ''.join(secrets.choice(caracteres) for _ in range(longueur))
st.code(password)
st.progress( min(longueur / 32, 1))
st.button("Nouveau mot de passe")