import streamlit as st
import numpy as np
st.set_page_config(page_icon="🌦", page_title="DASHBOARD METEO", layout="wide")
st.title("Dashboard méteo")
ville = st.selectbox("ville",["lome","kara","Atakpame","Sokode", "Bassar", "Kabou", "Dapaong", "Mango" , "Pia", "Niamtougou"])
temperatures = np.random.randint(10, 30, size=7)
humidite = np.random.randint(40, 100, size=7)
vent = np.random.randint(5, 25, size=7)
st.metric("Température", f"{temperatures[-1]}°C")
delta=int(temperatures[-1]-temperatures[-2])
st.write(f"humidité:{humidite[-1]} %")
st.write(f"vent:{vent[-1]} km/h")
st.line_chart(temperatures)