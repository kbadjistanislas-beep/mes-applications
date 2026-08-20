import streamlit as st
import string
import secrets

st.set_page_config(
    page_title="Générateur de mots de passe",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Générateur de mots de passe")
st.write("Crée un mot de passe sécurisé et personnalisable.")

# Fonction pour générer un mot de passe
def generer_mot_de_passe(longueur, chiffres, symboles):
    caracteres = string.ascii_letters

    if chiffres:
        caracteres += string.digits

    if symboles:
        caracteres += string.punctuation

    return "".join(
        secrets.choice(caracteres)
        for _ in range(longueur)
    )


# Paramètres
longueur = st.slider(
    "Longueur du mot de passe",
    min_value=6,
    max_value=64,
    value=16
)

chiffres = st.checkbox(
    "Inclure des chiffres",
    value=True
)

symboles = st.checkbox(
    "Inclure des symboles",
    value=True
)


# Générer le premier mot de passe
if "password" not in st.session_state:
    st.session_state.password = generer_mot_de_passe(
        longueur,
        chiffres,
        symboles
    )


# Bouton de génération
if st.button(
    "🔄 Nouveau mot de passe",
    use_container_width=True
):
    st.session_state.password = generer_mot_de_passe(
        longueur,
        chiffres,
        symboles
    )


# Affichage
st.subheader("Votre mot de passe")

st.code(
    st.session_state.password,
    language=None
)


# Estimation simple de la force
password = st.session_state.password

force = 0

if len(password) >= 12:
    force += 1

if any(c.islower() for c in password):
    force += 1

if any(c.isupper() for c in password):
    force += 1

if any(c.isdigit() for c in password):
    force += 1

if any(c in string.punctuation for c in password):
    force += 1


if force <= 2:
    st.warning("🟠 Mot de passe faible")

elif force <= 4:
    st.info("🟡 Mot de passe moyen")

else:
    st.success("🟢 Mot de passe très fort")


st.progress(force / 5)
