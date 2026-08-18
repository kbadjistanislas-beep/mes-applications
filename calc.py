import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Initialisation
if 'ecran' not in st.session_state:
    st.session_state.ecran = ''

st.title("🧮 Calculatrice + Graphique")

# ===== PARTIE 1 : CALCULATRICE =====
st.write("### Calculatrice")
st.text_input("", value=st.session_state.ecran, disabled=True)

# Boutons en 4 colonnes
c1, c2, c3, c4 = st.columns(4)

with c1:
    for b in ['1','2','3']:
        if st.button(b):
            st.session_state.ecran += b
            st.rerun()

with c2:
    for b in ['4','5','6']:
        if st.button(b):
            st.session_state.ecran += b
            st.rerun()

with c3:
    for b in ['7','8','9']:
        if st.button(b):
            st.session_state.ecran += b
            st.rerun()

with c4:
    for b in ['+','-','*','/']:
        if st.button(b):
            st.session_state.ecran += b
            st.rerun()

# Boutons spéciaux
if st.button('0'):
    st.session_state.ecran += '0'
    st.rerun()

if st.button('.'):
    st.session_state.ecran += '.'
    st.rerun()

if st.button('='):
    try:
        st.session_state.ecran = str(eval(st.session_state.ecran))
    except:
        st.warning("Erreur")
    st.rerun()

if st.button('C'):
    st.session_state.ecran = ''
    st.rerun()

# ===== PARTIE 2 : TRACER UNE FONCTION =====
st.write("### Tracer une fonction")
fonction = st.text_input("Entrez f(x) (ex: x**2, 2*x+1, sin(x))")

if fonction:
    if st.button("📈 Tracer"):
        try:
            x = np.linspace(-10, 10, 100)
            # Remplacer les fonctions pour qu'elles fonctionnent
            f = fonction.replace('sin', 'np.sin')
            f = f.replace('cos', 'np.cos')
            f = f.replace('sqrt', 'np.sqrt')
            f = f.replace('log', 'np.log')
            y = eval(f)
            
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.grid(True)
            ax.axhline(y=0, color='black', alpha=0.3)
            ax.axvline(x=0, color='black', alpha=0.3)
            st.pyplot(fig)
        except:
            st.warning("Erreur dans la fonction")