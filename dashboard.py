import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Météo Togo", page_icon="🌤️", layout="wide")

villes = ["Lomé", "Atakpamé", "Kara", "Sokodé", "Kpalimé", "Tsévié", "Aného", "Dapaong", "Bassar", "Niamtougou", "Bafilo", "Mango", "Tchaoudjo", "Sotouboua", "Tchamba", "Notsé", "Amou", "Amlamé", "Sagbado", "Agbélouvé", "Badou", "Elavagnon", "Tandjouaré", "Goubi", "Cinkassé"]

st.title("🌤️ Météo Togo")

ville = st.selectbox("Ville", villes)
jours = st.selectbox("Période", [7, 14, 30], index=0)

# Génération des données
np.random.seed(hash(ville) % 2**32)
base = 30 if ville in ["Lomé", "Aného", "Tsévié", "Kpalimé"] else 35 if ville in ["Kara", "Dapaong", "Mango", "Cinkassé"] else 33
temp = np.random.randint(base-5, base+5, jours)
humid = np.random.randint(50 if ville in ["Lomé", "Aného", "Tsévié"] else 40, 90, jours)
vent = np.random.randint(5, 30, jours)

# Métriques
c1, c2, c3 = st.columns(3)
c1.metric("🌡️ Temp", f"{temp[-1]}°C", f"{temp[-1]-temp[-2]:+.1f}°C")
c2.metric("💧 Humidité", f"{humid[-1]}%", f"{humid[-1]-humid[-2]:+.0f}%")
c3.metric("💨 Vent", f"{vent[-1]} km/h", f"{vent[-1]-vent[-2]:+.0f} km/h")

# Graphique
st.line_chart(pd.DataFrame({"Température": temp, "Humidité": humid, "Vent": vent}))

# Données
with st.expander("📋 Détails"):
    st.dataframe(pd.DataFrame({
        "Date": [(datetime.now() - timedelta(days=i)).strftime("%d/%m") for i in range(jours-1, -1, -1)],
        "Temp": temp,
        "Humidité": humid,
        "Vent": vent
    }))