import streamlit as st
import flitz 
import base64
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
    st.divider()
    st.subheader("📊 Informations du PDF")

    taille = len(pdf.getvalue()) / 1024
    texte_total = "".join(page.get_text() for page in docu)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("📄 Pages", len(docu))

    with c2:
        st.metric("📝 Caractères", len(texte_total))

    with c3:
        st.metric("💾 Taille", f"{taille:.1f} Ko")
        if "page" not in st.session_state:
            st.session_state.page = 1

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅️"):
            st.session_state.page = max(1, st.session_state.page - 1)

    with col2:
        st.session_state.page = st.number_input(
            "Page",
            1,
            len(docu),
            st.session_state.page
        )

    with col3:
        if st.button("➡️"):
            st.session_state.page = min(
                len(docu),
                st.session_state.page + 1
            )
    with st.sidebar:
        st.header("⚙️ Options")
        recherche = st.text_input("🔎 Rechercher")

        if recherche:
            resultats = []

            for i, p in enumerate(docu):
                if recherche.lower() in p.get_text().lower():
                    resultats.append(i + 1)

            if resultats:
                st.success(f"Pages : {resultats}")
            else:
                st.warning("Introuvable")
    texte_page = docu[st.session_state.page - 1].get_text()

    st.subheader(f"📄 Page {st.session_state.page}")
    st.write(texte_page[:2000])
  
    texte_page = docu[page - 1].get_text()
    st.subheader(f"Page {page}")
    st.write(texte_page[:2000])
    st.divider()
    st.subheader("📖 Aperçu du document")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ⏮️ Début du PDF")
        texte_debut = docu[0].get_text()
        st.text_area(
            "Première page",
            texte_debut[:2000],
            height=300
        )

    with col2:
        st.markdown("### ⏭️ Fin du PDF")
        texte_fin = docu[-1].get_text()
        st.text_area(
            "Dernière page",
            texte_fin[:2000],
            height=300
        )
    st.divider()
    st.subheader("📥 Extraire le texte")

    texte_total = "".join(page.get_text() for page in docu)

    st.download_button(
        "⬇️ Télécharger le texte",
        texte_total,
        file_name="texte_pdf.txt",
        mime="text/plain"
)
    st.divider()
    st.subheader("🔎 Rechercher dans le PDF")

    recherche = st.text_input("Mot à rechercher")

    if recherche:
        resultats = []

        for i, p in enumerate(docu):
            if recherche.lower() in p.get_text().lower():
                resultats.append(i + 1)

        if resultats:
            st.success(f"Trouvé aux pages : {resultats}")
        else:
            st.warning("Mot introuvable")
    st.divider()
    st.subheader("📖 Lecteur PDF")

    with open("document.pdf", "rb") as f:
        pdf_data = f.read()

    st.download_button(
        "⬇️ Télécharger le PDF",
        pdf_data,
        file_name="document.pdf",
        mime="application/pdf"
    )
    pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")

    pdf_viewer = f"""
    <iframe
        src="data:application/pdf;base64,{pdf_base64}"
        width="100%"
        height="700"
        type="application/pdf">
    </iframe>
    """

    st.markdown(pdf_viewer, unsafe_allow_html=True)
    st.divider()
    st.subheader("📝 Résumé rapide")

    phrases = texte_total.replace("\n", " ").split(".")
    resume = ". ".join(
        phrase.strip()
        for phrase in phrases
        if phrase.strip()
    )[:1000]

    st.write(resume + "...")
    st.divider()
    st.subheader("🔎 Rechercher dans le PDF")

    recherche = st.text_input("Entrez un mot ou une phrase")

    if recherche:
        resultats = []

        for i, page in enumerate(docu):
            texte = page.get_text()

            if recherche.lower() in texte.lower():
                resultats.append(i + 1)

        if resultats:
            st.success(
                f"✅ {len(resultats)} page(s) trouvée(s) : {resultats}"
            )
        else:
            st.warning("❌ Aucun résultat trouvé.")