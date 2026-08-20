import streamlit as st

with st.sidebar:
    st.title("Mes Applis")
    st.divider()
    st.caption("Version 1.5")

st.set_page_config(
    page_title="Carte de visite",
    page_icon="📇",
    layout="wide"
)

# Définition des pages avec des chemins relatifs depuis la racine
visit_card = st.Page("app.py", title="Carte de visite", icon="📇")

convert = st.Page('convertir.py', title = 'Convertisseur', icon='🧮')
calculatrice = st.Page('calculatrice.py', title='Calculatrice', icon='➕')
data = st.Page('explorateur.py', title='Data Explorer', icon='🔢')
todolist =  st.Page('to-do-list.py', title='Ma to-do', icon='👌')
passe =  st.Page('password.py', title='Mot de passe', icon='🤞')
visual = st.Page('visualiseur.py', title='View', icon='🥸')
meteo = st.Page('dashboard.py', title='Météo', icon='⛈️')
social = st.Page('rocial.py', title='Reseau social', icon='🤖')
fus = st.Page(
    "fusion.py",
    title="Fusionneur de PDF",
    icon=":material/picture_as_pdf:"
)

# Configuration de la navigation
pg = st.navigation([visit_card, convert, calculatrice, data, todolist, meteo, passe,social,visual,fus])

# Exécution de la page sélectionnée
pg.run()