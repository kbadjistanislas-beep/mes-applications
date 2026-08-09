import streamlit as st
import json,os
if 'posts' not in st.session_state:
    st.session_state.posts =[]
with st.form('post'):
    pseudo = st.text_input("Pseudo")
    message = st.text_area("Message")
    envoyer = st.form_submit_button("Publier")
if envoyer and pseudo and message:
    st.session_state.posts.insert(0, {"pseudo":pseudo,"message": message, "likes":0})
for per in st.session_state.posts:
    with st.container(border=True):
        st.write(f"**{per['pseudo']}**")
        st.writte(per["message"])
        if st.button(f"{per['likes']}"):
            per["likes"] += 1