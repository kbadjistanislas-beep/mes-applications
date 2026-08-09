import streamlit as st
import pandas as pd
@st.cache_data
def charger_donnees():
    return pd.read_csv("data.csv")

df = charger_donnees()
st.title("Visualisateur de donnees")
categorie = st.sidebar.multiselect("Categories", df["categorie"].unique())
if categorie:
    df = df[df["categorie"].isin(categorie)]
st.dataframe(df)
st.bar_chat(df, x="categorie", y="valeur")
    

