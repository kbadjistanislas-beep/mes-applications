import streamlit as st
import pandas as pd
st.title("Explorateur de Dataset CSV")
fichier = st.file_uploader("Choisir un fichier CSV", type="csv")
if fichier is not None:
    df = pd.read_csv(fichier)
    st.dataframe(df)
    coln1, coln2 = st.columns(2)
    with coln1:
        st.metric("Nombre de lignes", df.shape[0])
    with coln2:
        st.metric("Nombre de colones", df.shape[1])
    st.subheader("Statistiques descriptives")
    st.dataframe(df.describe())
    st.subheader("Selectionner les colones a afficher")
    colones = st.multiselect("Choisissez les colones", df.columns.tolist(), default=df.columns.tolist())
    if colones:
        st.dataframe(df[colones])
    else:
        st.write("Veuillez selectionner au moins une colones.")
else:
    st.write("Fichier non trouve")