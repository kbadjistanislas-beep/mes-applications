import streamlit as st
import math
import plotly.graph_objects as np
import numpy as np
if "historique" not in st.session_state:
    st.session_state.historique = []
st.set_page_config(page_title="Calculatrice" , page_icon="🧮" , layout="wide" )
st.markdown("""
<style>
.calculatrice {
    max-width: 600px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)
if "calcul" not in st.session_state:
        st.session_state.calcul = ""
st.title("🧮 CALCULATRICE SCIENTIFIQUE")
st.caption("Calculs • Fonctions scientifiques • Graphiques")
st.text_input(
    "Écran",
    st.session_state.calcul,
    disabled=True,
    placeholder="0"
)
angle = st.radio("Mode angle", ["Degrés", "Radians"], horizontal=True)
def bouton(valeur):
        st.sesion_state.calcul += valeur 
coln1,coln2,coln3,coln4 =st.columns(4)
with coln1:
        for bouton in ['7', '4', '1', '0']:
            if st.button(bouton):
                st.session_state.calcul += bouton
                st.rerun()  

with coln2:
        for bouton in ['8', '5', '2', '.']:
            if st.button(bouton):
                st.session_state.calcul += bouton
                st.rerun()  
with coln3:
       for bouton in ['9', '6', '3', '+']:
        if st.button(bouton):
            st.session_state.calcul += bouton
            st.rerun()  
with coln4:
        for bouton in ['/', '*', '-', '..']:
            if st.button(bouton):
                st.session_state.calcul += bouton
                st.rerun()  
if st.button("AC"):
        st.session_state.calcul = ""
        st.rerun()
if st.button("⌫"):
    st.session_state.calcul = st.session_state.calcul[:-1]
    st.rerun()
st.subheader("Fonctions scientifiques")                
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("√"):
        bouton("sqrt(")
    if st.button("sin"):
        bouton("sin(")

with c2:
    if st.button("x²"):
        bouton("**2")
    if st.button("cos"):
        bouton("cos(")

with c3:
    if st.button("xʸ"):
        bouton("**")
    if st.button("tan"):
        bouton("tan(")

with c4:
    if st.button("log"):
        bouton("log(")
    if st.button("ln"):
        bouton("ln(")

with c5:
    if st.button("π"):
        bouton("pi")
    if st.button("e"):
        bouton("e")
try:
        resultat = eval(st.session_state.calcul,
                {"__builtins__": {}},
                {   "sqrt": math.sqrt,
                "sin": lambda x: math.sin(math.radians(x)) if angle == "Degrés" else math.sin(x),
"cos": lambda x: math.cos(math.radians(x)) if angle == "Degrés" else math.cos(x),
"tan": lambda x: math.tan(math.radians(x)) if angle == "Degrés" else math.tan(x),
                "log": math.log10,
                "ln": math.log,
                "pi": math.pi,
                "e": math.e  }
                )
        st.session_state.historique.append(
    f"{st.session_state.calcul} = {resultat}"
)
        st.session_state.calcul = str(resultat)
        st.rerun()
except:
        st.session_state.calcul = "Erreur"
        st.rerun()
st.divider()

mode = st.radio(
    "Mode",
    ["🧮 Calculatrice", "📈 Graphique"],
    horizontal=True
)
st.subheader("📈 Tracer une fonction")

fonction = st.text_input("f(x) =", "x**2")

if st.button("📈 Tracer"):
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(fonction, {"__builtins__": {}}, {"x": x, "np": np})

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
        fig.update_layout(
            xaxis_title="x",
            yaxis_title="f(x)",
            title=f"f(x) = {fonction}"
        )

        st.plotly_chart(fig, use_container_width=True)

    except:
        st.error("Fonction invalide")
st.divider()
st.subheader("📜 Historique")

for calcul in reversed(st.session_state.historique):
    st.write(calcul)

if st.button("🗑️ Effacer l'historique"):
    st.session_state.historique = []
    st.rerun()