import streamlit as st
import json
import os

st.set_page_config(page_title="To-Do", page_icon="✅")

FICHIER = "taches.json"

# Charger
if "taches" not in st.session_state:
    st.session_state.taches = json.load(open(FICHIER)) if os.path.exists(FICHIER) else []

# Ajouter
with st.form("form"):
    titre = st.text_input("Tâche")
    priorite = st.selectbox("Priorité", ["Basse", "Moyenne", "Haute"])
    if st.form_submit_button("➕ Ajouter") and titre:
        st.session_state.taches.append({
            "titre": titre,
            "priorite": priorite,
            "terminee": False
        })
        json.dump(st.session_state.taches, open(FICHIER, "w"))
        st.rerun()

# Afficher
st.title("✅ To-Do-List")
for i, tache in enumerate(st.session_state.taches):
    # ✅ La clé 'key' évite les conflits d'ID
    terminee = st.checkbox(
        f"{tache['priorite']} - {tache['titre']}",
        value=tache.get("terminee", False),
        key=f"check_{i}"  # ← La solution
    )
    
    # Sauvegarder si l'état change
    if terminee != tache.get("terminee", False):
        tache["terminee"] = terminee
        json.dump(st.session_state.taches, open(FICHIER, "w"))
        st.rerun()

# Progression
if st.session_state.taches:
    total = len(st.session_state.taches)
    terminees = sum(1 for t in st.session_state.taches if t.get("terminee", False))
    progress = terminees / total
    st.progress(progress)
    st.write(f"**{int(progress*100)}%** terminé ({terminees}/{total})")
    if progress == 1:
        st.balloons()