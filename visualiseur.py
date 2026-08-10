import streamlit as st
import pandas as pd
st.title("Visualiseur de données")

fichier = st.file_uploader(
        "Importer votre fichier CSV",
        type=["csv"]
    )

if fichier is not None:
        df = pd.read_csv(fichier)

        categorie = st.sidebar.multiselect(
            "Categories",
            df["categorie"].unique()
        )

        if categorie:
            df = df[df["categorie"].isin(categorie)]

        st.dataframe(df)

        st.bar_chart(
            df,
            x="categorie",
            y="valeur"
        )


