import streamlit as st
import flitz 
st.title("Analyseur PDF")
with st.form("upload"):
    pdf = st.file_uploader("Choisir un PDF", type="pdf")
    uploader = st.form_submit_button("Upload")
if uploader and pdf :
    with open("document.pdf","wb") as f:
        f.write(pdf.getvalue())
    docu = flitz.open("document.pdf")
    st.success("PDF importer ")
    st.writte(f"{len(docu)} pages")

    st.subheader("Debut")
    texte_debut = docu[0].get_text()
    st.write(texte_debut[:1000])
    st.subheader("Fin")
    texte_fin = docu[-1].get_text()
    st.write(texte_fin[:1000])