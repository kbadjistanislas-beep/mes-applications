import json,os
import streamlit as st
def charger_test():
        if os.path.exists("taches.json"):
            with open("taches.json") as f:return json.load(f)
        return []
def sauvegarder_taches(tach):
        with open("taches.json", "w") as f:json.dump(tach, f)
taches = charger_test()
st.title("To-Do-List")
with st.form("from"):
        titre = st.text_input("Tache")
        priorite = st.selectbox("Priorite", ["Basse", "Moyenne", "Haute"])
        if st.form_submit_button("Ajouter") and titre:
            taches.append({"titre":titre, "priorite":priorite, "terminee":False})
            sauvegarder_taches(taches);st.rerun()
for i,tach in enumerate(taches):
        tach["terminee"] = st.checkbox(f'{tach["titre"]} ({tach["priorite"]})', tach["terminee"],key=i)
sauvegarder_taches(taches)
st.progress(sum(tach["terminee"] for tach in taches) / len(taches) if taches else 0)
st.balloons()