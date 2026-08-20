import streamlit as st
from pypdf import PdfWriter
from pathlib import Path

st.set_page_config(page_title="Fusion PDF", page_icon="📄")

st.title("📄 Fusionneur de PDF")

# 1. Importer les fichiers
st.subheader("1️⃣ Choisissez vos PDF")
fichiers = st.file_uploader(
    "Sélectionnez vos PDF",
    type="pdf",
    accept_multiple_files=True
)

# 2. Afficher les fichiers choisis
if fichiers:
    st.write(f"📁 {len(fichiers)} fichier(s) sélectionné(s)")
    for f in fichiers:
        st.write(f"   - {f.name}")

# 3. Bouton pour fusionner
st.subheader("2️⃣ Fusionner")
if st.button("🔄 Fusionner les PDF"):
    if not fichiers:
        st.warning("⚠️ Veuillez sélectionner au moins 2 PDF")
    elif len(fichiers) < 2:
        st.warning("⚠️ Il faut au moins 2 PDF pour fusionner")
    else:
        with st.spinner("Fusion en cours..."):
            try:
                # Créer un dossier temporaire
                dossier_temp = Path("temp_fusion")
                dossier_temp.mkdir(exist_ok=True)
                
                # Créer le fusionneur
                mergeur = PdfWriter()
                
                # Ajouter chaque fichier
                for f in fichiers:
                    chemin_temp = dossier_temp / f.name
                    with open(chemin_temp, "wb") as fichier_temp:
                        fichier_temp.write(f.read())
                    mergeur.append(str(chemin_temp))
                
                # Créer le fichier final
                chemin_sortie = dossier_temp / "fusion.pdf"
                with open(chemin_sortie, "wb") as fichier_sortie:
                    mergeur.write(fichier_sortie)
                mergeur.close()
                
                # Lire le fichier fusionné
                with open(chemin_sortie, "rb") as fichier_sortie:
                    donnees = fichier_sortie.read()
                
                # Nettoyer (supprimer les fichiers temporaires)
                for fichier in dossier_temp.glob("*"):
                    fichier.unlink()
                dossier_temp.rmdir()
                
                # Succès
                st.success("✅ Fusion réussie !")
                
                # Bouton pour télécharger
                st.download_button(
                    label="📥 Télécharger la fusion",
                    data=donnees,
                    file_name="fusion.pdf",
                    mime="application/pdf"
                )
                
            except Exception as e:
                st.error(f"❌ Erreur : {e}")