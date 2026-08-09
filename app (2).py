import streamlit as st
st.set_page_config(page_title="Carte de visite", page_icon="🃏" ,layout="wide")
coln1 , coln2 = st.columns(2)
with coln1:
    st.image("photo8.jpeg")
with coln2:
    st.title("KPANTE Badji Stanislas")
    st.subheader("Developpeur Python et Data Scientist")
    st.write("Jeune developpeur en evolution progressive")
    st.markdown("[Mon Github] (https://github.com/kbadjistanislas-beep)")