import streamlit as st
import json
import os

# Initialisation des posts
if "posts" not in st.session_state:
    st.session_state.posts = []

# Formulaire pour publier
with st.form("post"):
    pseudo = st.text_input("Pseudo")
    message = st.text_area("Message")
    envoyer = st.form_submit_button("Publier")

# Création d'un nouveau post
if envoyer and pseudo and message:
    st.session_state.posts.insert(0, {
        "pseudo": pseudo,
        "message": message,
        "likes": 0,
        "liked_by": []
    })

# Affichage des posts
for i, per in enumerate(st.session_state.posts):

    # Pour les anciens posts qui n'ont pas encore "liked_by"
    if "liked_by" not in per:
        per["liked_by"] = []

    with st.container(border=True):

        st.write(f"**{per['pseudo']}**")
        st.write(per["message"])

        # Vérifie si le pseudo a déjà liké
        deja_like = pseudo in per["liked_by"]

        if st.button(
            f"❤️ {per['likes']}",
            key=f"like_{i}",
            disabled=deja_like or not pseudo
        ):
            per["likes"] += 1
            per["liked_by"].append(pseudo)

            st.rerun()
