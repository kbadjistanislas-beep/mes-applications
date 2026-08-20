import streamlit as st

st.set_page_config(page_title="Convertisseur", page_icon="📐", layout="centered")

st.title("📐 Convertisseur Universel")

# ==================== DONNÉES ====================
unites = {
    "📏 Longueur": {"m":1, "cm":0.01, "mm":0.001, "km":1000, "pouce":0.0254, "pied":0.3048},
    "⚖️ Poids": {"kg":1, "g":0.001, "mg":0.000001, "tonne":1000, "livre":0.453592},
    "🌡️ Température": ["°C", "°F", "K"],
    "📊 Superficie": {"m²":1, "cm²":0.0001, "km²":1000000, "hectare":10000},
    "🧊 Volume": {"L":1, "mL":0.001, "m³":1000, "gal":3.78541}
}

# ==================== INTERFACE ====================
cat = st.selectbox("📂 Catégorie", list(unites.keys()))

if cat == "🌡️ Température":
    unites_cat = unites[cat]
    col1, col2 = st.columns(2)
    d = col1.selectbox("De", unites_cat)
    a = col2.selectbox("À", unites_cat)
    v = st.number_input("🔢 Valeur", value=0.0, step=0.1, format="%.2f")
    
    # Conversion température
    if d == a:
        r = v
    elif d == "°C" and a == "°F":
        r = (v * 9/5) + 32
    elif d == "°F" and a == "°C":
        r = (v - 32) * 5/9
    elif d == "°C" and a == "K":
        r = v + 273.15
    elif d == "K" and a == "°C":
        r = v - 273.15
    elif d == "°F" and a == "K":
        r = (v - 32) * 5/9 + 273.15
    elif d == "K" and a == "°F":
        r = (v - 273.15) * 9/5 + 32
    else:
        r = v
    
else:
    facteurs = unites[cat]
    cols = st.columns(3)
    d = cols[0].selectbox("De", list(facteurs.keys()))
    a = cols[1].selectbox("À", list(facteurs.keys()))
    v = cols[2].number_input("Valeur", value=1.0, step=0.1)
    
    # Conversion standard
    r = v * (facteurs[a] / facteurs[d])

# ==================== RÉSULTAT ====================
st.divider()
col_res1, col_res2, col_res3 = st.columns([1, 2, 1])

with col_res2:
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#667eea,#764ba2);padding:25px;border-radius:15px;text-align:center;color:white;'>
        <h2>{v} {d} = {r:.4f} {a}</h2>
        <p style='margin:0;opacity:0.8;'>Conversion effectuée avec succès ✅</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TABLEAU DES ÉQUIVALENCES ====================
with st.expander("📋 Voir toutes les équivalences"):
    st.write(f"**{v} {d}** équivaut à :")
    if cat == "🌡️ Température":
        for u in unites_cat:
            if u != d:
                if u == "°F":
                    r2 = (v * 9/5) + 32 if d == "°C" else (v - 273.15) * 9/5 + 32 if d == "K" else v
                elif u == "K":
                    r2 = v + 273.15 if d == "°C" else (v - 32) * 5/9 + 273.15 if d == "°F" else v
                else:
                    r2 = (v - 32) * 5/9 if d == "°F" else v - 273.15 if d == "K" else v
                st.write(f"- {r2:.4f} {u}")
    else:
        for u, f in facteurs.items():
            if u != d:
                r2 = v * (f / facteurs[d])
                st.write(f"- {r2:.4f} {u}")

# ==================== HISTORIQUE ====================
if "historique" not in st.session_state:
    st.session_state.historique = []

if st.button("💾 Enregistrer"):
    st.session_state.historique.append(f"{v} {d} = {r:.4f} {a}")
    st.success("✅ Enregistré !")

if st.session_state.historique:
    with st.expander(f"📜 Historique ({len(st.session_state.historique)})"):
        for item in reversed(st.session_state.historique[-10:]):
            st.write(f"- {item}")
        if st.button("🗑️ Effacer"):
            st.session_state.historique = []
            st.rerun()

# ==================== RACCOURCIS ====================
st.caption("💡 Astuce : Utilisez les flèches pour ajuster la valeur rapidement")