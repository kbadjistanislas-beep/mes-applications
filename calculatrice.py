import streamlit as st
import math
import plotly.graph_objects as go
import numpy as np
import re

# ==================== CONFIGURATION ====================
st.set_page_config(
    page_title="Calculatrice Scientifique",
    page_icon="🧮",
    layout="wide"
)

# ==================== CSS PERSONNALISÉ ====================
st.markdown("""
<style>
    .calculatrice {
        max-width: 600px;
        margin: auto;
        padding: 20px;
    }
    .stButton button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
    }
    .ecran {
        background-color: #1e1e1e;
        color: #00ff00;
        padding: 20px;
        border-radius: 10px;
        font-size: 28px;
        text-align: right;
        font-family: 'Courier New', monospace;
        min-height: 80px;
        border: 2px solid #333;
    }
    .historique-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        max-height: 300px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INITIALISATION SESSION ====================
if "calcul" not in st.session_state:
    st.session_state.calcul = ""
if "historique" not in st.session_state:
    st.session_state.historique = []
if "mode_angle" not in st.session_state:
    st.session_state.mode_angle = "Degrés"
if "dernier_resultat" not in st.session_state:
    st.session_state.dernier_resultat = None

# ==================== TITRE ====================
st.title("🧮 CALCULATRICE SCIENTIFIQUE")
st.caption("Calculs • Fonctions scientifiques • Graphiques • Historique")

# ==================== ÉCRAN ====================
col_ecran1, col_ecran2 = st.columns([4, 1])
with col_ecran1:
    st.markdown(f"""
    <div class="ecran">
        {st.session_state.calcul if st.session_state.calcul else "0"}
    </div>
    """, unsafe_allow_html=True)

with col_ecran2:
    st.caption("Résultat")
    if st.session_state.dernier_resultat is not None:
        st.markdown(f"**= {st.session_state.dernier_resultat}**")

# ==================== MODE ANGLE ====================
st.session_state.mode_angle = st.radio(
    "Mode angle",
    ["Degrés", "Radians"],
    horizontal=True,
    key="angle_radio"
)

# ==================== FONCTION BOUTON ====================
def ajouter_texte(valeur):
    """Ajoute du texte à l'écran"""
    st.session_state.calcul += valeur

def ajouter_parenthese_fermante():
    """Ajoute une parenthèse fermante automatiquement"""
    # Compter les parenthèses ouvertes et fermées
    ouvert = st.session_state.calcul.count('(')
    ferme = st.session_state.calcul.count(')')
    if ouvert > ferme:
        st.session_state.calcul += ')'
    else:
        st.session_state.calcul += '('

# ==================== BOUTONS NUMÉRIQUES ====================
st.subheader("🔢 Nombres et opérateurs")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    for btn in ['7', '4', '1', '0']:
        if st.button(btn, key=f"num_{btn}"):
            ajouter_texte(btn)

with col2:
    for btn in ['8', '5', '2', '.']:
        if st.button(btn, key=f"num_{btn}"):
            ajouter_texte(btn)

with col3:
    for btn in ['9', '6', '3', '=']:
        if st.button(btn, key=f"num_{btn}"):
            if btn == '=':
                st.rerun()
            else:
                ajouter_texte(btn)

with col4:
    for btn in ['+', '-', '*', '/']:
        if st.button(btn, key=f"op_{btn}"):
            ajouter_texte(btn)

with col5:
    if st.button("AC", key="ac"):
        st.session_state.calcul = ""
        st.session_state.dernier_resultat = None
        st.rerun()
    if st.button("⌫", key="backspace"):
        st.session_state.calcul = st.session_state.calcul[:-1]
        st.rerun()
    if st.button("( )", key="parentheses"):
        ajouter_parenthese_fermante()

# ==================== FONCTIONS SCIENTIFIQUES ====================
st.subheader("📐 Fonctions scientifiques")

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("√", key="sqrt"):
        ajouter_texte("sqrt(")
    if st.button("x²", key="square"):
        ajouter_texte("**2")

with c2:
    if st.button("sin", key="sin"):
        ajouter_texte("sin(")
    if st.button("cos", key="cos"):
        ajouter_texte("cos(")

with c3:
    if st.button("tan", key="tan"):
        ajouter_texte("tan(")
    if st.button("xʸ", key="power"):
        ajouter_texte("**")

with c4:
    if st.button("log₁₀", key="log10"):
        ajouter_texte("log10(")
    if st.button("ln", key="ln"):
        ajouter_texte("ln(")

with c5:
    if st.button("π", key="pi"):
        ajouter_texte("pi")
    if st.button("e", key="euler"):
        ajouter_texte("e")

with c6:
    if st.button("1/x", key="inverse"):
        ajouter_texte("1/")
    if st.button("!", key="factorial"):
        ajouter_texte("factorial(")

# ==================== ÉVALUATION ====================
def evaluer_expression(expression):
    """Évalue l'expression mathématique avec sécurité"""
    try:
        # Définir les fonctions autorisées
        fonctions_autorisees = {
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)) if st.session_state.mode_angle == "Degrés" else math.sin(x),
            "cos": lambda x: math.cos(math.radians(x)) if st.session_state.mode_angle == "Degrés" else math.cos(x),
            "tan": lambda x: math.tan(math.radians(x)) if st.session_state.mode_angle == "Degrés" else math.tan(x),
            "log10": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial,
            "abs": abs,
            "round": round,
            "max": max,
            "min": min
        }
        
        # Évaluer
        resultat = eval(expression, {"__builtins__": {}}, fonctions_autorisees)
        return resultat
    except Exception as e:
        return None

# Bouton pour calculer
col_calc1, col_calc2 = st.columns([1, 3])
with col_calc1:
    if st.button("🟢 Calculer", type="primary", use_container_width=True):
        if st.session_state.calcul:
            resultat = evaluer_expression(st.session_state.calcul)
            if resultat is not None:
                # Ajouter à l'historique
                st.session_state.historique.append(
                    f"{st.session_state.calcul} = {resultat}"
                )
                st.session_state.dernier_resultat = resultat
                st.session_state.calcul = str(resultat)
                st.rerun()
            else:
                st.error("❌ Expression invalide")
                st.session_state.calcul = "Erreur"
                st.rerun()

with col_calc2:
    if st.button("🧹 Effacer", use_container_width=True):
        st.session_state.calcul = ""
        st.session_state.dernier_resultat = None
        st.rerun()

# ==================== DIVISEUR ====================
st.divider()

# ==================== MODE ====================
mode = st.radio(
    "Mode",
    ["🧮 Calculatrice", "📈 Graphique"],
    horizontal=True
)

# ==================== GRAPHIQUE ====================
if mode == "📈 Graphique":
    st.subheader("📈 Tracer une fonction")
    
    col_f1, col_f2 = st.columns([3, 1])
    with col_f1:
        fonction = st.text_input("f(x) =", "x**2 + sin(x)")
    
    with col_f2:
        st.write("")
        st.write("")
        if st.button("📈 Tracer", type="primary", use_container_width=True):
            try:
                # Générer les données
                x = np.linspace(-10, 10, 500)
                y = eval(fonction, {"__builtins__": {}}, {
                    "x": x,
                    "np": np,
                    "sin": np.sin,
                    "cos": np.cos,
                    "tan": np.tan,
                    "sqrt": np.sqrt,
                    "exp": np.exp,
                    "log": np.log,
                    "log10": np.log10,
                    "abs": np.abs,
                    "pi": np.pi,
                    "e": np.e
                })
                
                # Créer le graphique
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=x,
                    y=y,
                    mode="lines",
                    name=f"f(x) = {fonction}",
                    line=dict(color="#667eea", width=3)
                ))
                
                # Mise en page
                fig.update_layout(
                    title=f"f(x) = {fonction}",
                    xaxis_title="x",
                    yaxis_title="f(x)",
                    template="plotly_white",
                    height=500,
                    hovermode="x",
                    xaxis=dict(gridcolor="#eee"),
                    yaxis=dict(gridcolor="#eee")
                )
                
                # Ajouter un point sur l'axe des x
                fig.add_hline(y=0, line_color="gray", line_width=1, opacity=0.5)
                fig.add_vline(x=0, line_color="gray", line_width=1, opacity=0.5)
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Afficher quelques valeurs
                st.caption(f"Valeurs : min = {y.min():.2f}, max = {y.max():.2f}, moyenne = {y.mean():.2f}")
                
            except Exception as e:
                st.error(f"❌ Fonction invalide : {e}")

# ==================== HISTORIQUE ====================
st.divider()
st.subheader("📜 Historique des calculs")

if st.session_state.historique:
    # Afficher l'historique (du plus récent au plus ancien)
    with st.container():
        st.markdown('<div class="historique-box">', unsafe_allow_html=True)
        for calcul in reversed(st.session_state.historique):
            st.code(calcul, language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🗑️ Effacer l'historique", use_container_width=True):
        st.session_state.historique = []
        st.rerun()
else:
    st.info("Aucun calcul enregistré")

# ==================== RACCOURCIS CLAVIER (Astuce) ====================
with st.expander("💡 Raccourcis clavier"):
    st.markdown("""
    - **Entrée** : Valider le calcul
    - **Échap** : Effacer l'écran
    - **+ - * /** : Opérations
    - **0-9** : Chiffres
    - **.** : Virgule
    - **( )** : Parenthèses
    """)

# ==================== PIED DE PAGE ====================
st.divider()
st.caption("🔒 Tous les calculs sont effectués localement - Aucune donnée n'est envoyée")