import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Mémoire
if 'e' not in st.session_state:
    st.session_state.e = ''

st.title("🧮 Calculatrice")

# Écran
st.text_input("", st.session_state.e, disabled=True)

# Chiffres
c1, c2, c3 = st.columns(3)
with c1:
    for b in ['1','2','3']:
        if st.button(b):
            st.session_state.e += b; st.rerun()
with c2:
    for b in ['4','5','6']:
        if st.button(b):
            st.session_state.e += b; st.rerun()
with c3:
    for b in ['7','8','9']:
        if st.button(b):
            st.session_state.e += b; st.rerun()

# Opérateurs
c4, c5, c6, c7 = st.columns(4)
with c4:
    if st.button('+'): st.session_state.e += '+'; st.rerun()
with c5:
    if st.button('-'): st.session_state.e += '-'; st.rerun()
with c6:
    if st.button('×'): st.session_state.e += '*'; st.rerun()
with c7:
    if st.button('÷'): st.session_state.e += '/'; st.rerun()

# Spéciaux
c8, c9, c10, c11 = st.columns(4)
with c8:
    if st.button('0'): st.session_state.e += '0'; st.rerun()
with c9:
    if st.button('.'): st.session_state.e += '.'; st.rerun()
with c10:
    if st.button('='):
        try:
            st.session_state.e = str(eval(st.session_state.e))
        except:
            st.warning("Erreur")
        st.rerun()
with c11:
    if st.button('C'): st.session_state.e = ''; st.rerun()

# Fonctions
st.write("---")
c12, c13, c14, c15, c16 = st.columns(5)
with c12:
    if st.button('sin'): st.session_state.e += 'sin('; st.rerun()
with c13:
    if st.button('cos'): st.session_state.e += 'cos('; st.rerun()
with c14:
    if st.button('√'): st.session_state.e += 'sqrt('; st.rerun()
with c15:
    if st.button('π'): st.session_state.e += '3.14'; st.rerun()
with c16:
    if st.button('²'): st.session_state.e += '**2'; st.rerun()

# Graphique
st.write("---")
f = st.text_input("Fonction (ex: x**2)")

if f and st.button("📊 Tracer"):
    try:
        x = np.linspace(-10, 10, 100)
        y = eval(f.replace('sin','np.sin').replace('cos','np.cos').replace('sqrt','np.sqrt'))
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.grid(True)
        ax.axhline(y=0, color='black', alpha=0.3)
        ax.axvline(x=0, color='black', alpha=0.3)
        st.pyplot(fig)
    except:
        st.warning("Erreur")