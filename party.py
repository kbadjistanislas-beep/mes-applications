import streamlit as st
st.title("Mes appnoz")
app = st.sidebar.radio("Menu", ["Calculatrice", "Meteo", "Quiz", "Password", "Convertisseur", "Carte de visite", "explorateur", "to-do-list", "visualiseur", "rocial"])
if app == "Calculatice":
    import streamlit as st

    if 'historique' not in st.session_state:
        st.session_state.h = []
    st.set_page_config(page_title="Calculatrice" , page_icon="🧮" , layout="wide" )
    st.title("CALCULATRICE")

    a = st.number_input("Nombre 1", value = 0.0 )
    b = st.number_input("Nombre 2", value = 0.0 )
    choix = st.selectbox("Operations" , ["+","-","*","/"])
    buton = st.button("=")
    if buton :
                if choix == "+":
                        st.write(f"resultat:{a+b}")
                elif choix == "-":
                        st.write(f"resultat:{a-b}")
                elif choix == "*":
                        st.write(f"resultat:{a*b}")
                elif choix == "/":
                        if b == 0:
                                st.write("operation impossible")
                        else: 
                            st.write(f"resultat:{round(a/b,3)}")
    else:
        st.write("operation non chargee")
elif app == "Meteo":
    import streamlit as st
    import numpy as np
    st.set_page_config(page_icon="🌦", page_title="DASHBOARD METEO", layout="wide")
    st.title("Dashboard méteo")
    ville = st.selectbox("ville",["lome","kara","Atakpame","Sokode", "Bassar", "Kabou", "Dapaong", "Mango" , "Pia", "Niamtougou"])
    temperatures = np.random.randint(10, 30, size=7)
    humidite = np.random.randint(40, 100, size=7)
    vent = np.random.randint(5, 25, size=7)
    st.metric("Température", f"{temperatures[-1]}°C")
    delta=int(temperatures[-1]-temperatures[-2])
    st.write(f"humidité:{humidite[-1]} %")
    st.write(f"vent:{vent[-1]} km/h")
    st.line_chart(temperatures)
elif app == "Quiz":
   import streamlit as st

score = 0

with st.form("quiz_form"):
        v1 = st.radio("Q1: Capitale de la France ?" , ["Paris","Marseille","Lyon"])
        v2 = st.radio("Q2: 8 + 5 = ?" , ["10","52","13"])
        v3 = st.radio("Q3: Language utilisé avec Streamlit", ["Python","java","C++"])
        v4 = st.radio("Q4: Capitale du canada", ["Toronto","Ottawa","Montréal"])
        v5 = st.radio("Q5: Mot-clé pour créer une fonction en Python ? ", ["func","def","fct"])

        valider = st.form_submit_button("valider")

if valider:
        if v1 == "Paris":
            score += 1
        if v2 == "13":
            score += 1
        if v3 == "Python":
            score += 1
        if v4 == "Ottawa":
            score += 1
        if v5 == "def":
            score += 1
        
        st.write("Score :", score, "/7")
        if score == 7:
            st.balloons()
            st.succes("Felicitations ! Score parfait.")
        else :
            st.warming("Continue tes efforts !") 
elif app == "Password":
    import streamlit as st
    import string, secrets
    longueur = st.slider("Longueur" , 6, 32, 12)
    caracteres = string.ascii_letters
    if st.checkbox("Inclure des chiffres"):
        caracteres += string.digits
    if st.checkbox("Inclure des symboles"):
        caracteres += string.punctuation
    password = ''.join(secrets.choice(caracteres) for _ in range(longueur))
    st.code(password)
    st.progress( min(longueur / 32, 1))
    st.button("Nouveau mot de passe")
elif app == "Conertisseur":
    import streamlit as st 
st.set_page_config(page_title="Convertisseur" , page_icon="💰", layout="wide")
st.subheader("CONVERTISSEUR")
choix = st.selectbox("Choisissez votre partie à convertir", ["longueur", "poids" , "temperature"])
valeur = st.number_input("entrez la valeur à convertir" , min_value=0, step= 100 )
unite_depart = st.selectbox("choiosisser l'unité de depart",["m","cm","kg","g","°C","°F"])
unite_arrivee = st.selectbox("choisissez l'unité d'arrivée", ["m","cm","kg","g","°C","°F"])
if choix == "longueur":
    if unite_depart == "m" and unite_arrivee == "cm":
        resultat = valeur * 100
    elif unite_depart == "cm" and unite_arrivee == "m":
        resultat = valeur / 1000
    elif unite_depart == unite_arrivee:
        resultat = valeur 
    else:
        st.error("conversion non supportée")
    st.write(f"le résultat est : {resultat} {unite_arrivee}")
elif  choix == "poids":
    if unite_depart == "kg" and unite_arrivee == "g":
            resultat = valeur * 100
    elif unite_depart == "g" and unite_arrivee == "kg":
            resultat = valeur / 1000
    elif unite_depart == unite_arrivee:
            resultat = valeur 
    else:
        st.error("conversion non supportée")
    st.write(f"le résultat est : {resultat} {unite_arrivee}")
elif choix == "temperature":
    if unite_depart == "°C" and unite_arrivee == "°F":
            resultat = (valeur * 9/5) + 32
    elif unite_depart == "°F" and unite_arrivee == "°C":
            resultat = (valeur - 32) * 5/9
    elif unite_depart == unite_arrivee:
            resultat = valeur 
    else:
        st.error("conversion non supportée")
    st.write(f"le résultat est : {resultat} {unite_arrivee}")

elif app == "Carte de visite":
    import streamlit as st
    st.set_page_config(page_title="Carte de visite", page_icon="🃏" ,layout="wide")
    coln1 , coln2 = st.columns(2)
    with coln1:
        st.image("photo8.jpeg")
    with coln2:
        st.title("KPANTE Badji Stanislas")
        st.subheader("Developpeur Python et Data Scientist")
        st.write("Jeune developpeur en evolution progressive")
        st.markdown("[Mon Github] (https://github.com/kbadjistanislas-beep)")
elif choix == "explorateur":
    import streamlit as st
    import pandas as pd
    st.title("Explorateur de Dataset CSV")
    fichier = st.file_uploader("Choisir un fichier CSV", type="csv")
    if fichier is not None:
        df = pd.read_csv(fichier)
        st.dataframe(df)
        coln1, coln2 = st.columns(2)
        with coln1:
            st.metric("Nombre de lignes", df.shape[0])
        with coln2:
            st.metric("Nombre de colones", df.shape[1])
        st.subheader("Statistiques descriptives")
        st.dataframe(df.describe())
        st.subheader("Selectionner les colones a afficher")
        colones = st.multiselect("Choisissez les colones", df.columns.tolist(), default=df.columns.tolist())
        if colones:
            st.dataframe(df[colones])
        else:
            st.write("Veuillez selectionner au moins une colones.")
    else:
        st.write("Fichier non trouve")
elif choix == "to-do-list":
    import json,os
    import streamlit as st
    def charger_test():
        if os.path.exists("taches.json"):
            with open("taches.json") as f:return json.load(f)
        return []
    def sauvegarder_taches(tach):
        with open("taches.json", "w") as f:json.dump(tach, f)
    taches = charger()
    st.title("To-Do-List")
    with st.form("from"):
        titre = st.text_input("Tache")
        priorite = st.selectbox("Priorite", ["Basse", "Moyenne", "Haute"])
        if st.form_submit_button("Ajouter") and titre:
            tache.append({"titre":titre, "priorite":priorite, "terminee":False})
            sauvegarder_taches(taches);st.rerun()
    for i,taches in enumerate(taches):
        tach["terminee"] = st.chec(f'{tach["titre"]} ({tach["priorite"]})', tach["terminee"],key=i)
    sauvegarder_taches(taches)
    st.progress(sum(tach["terminee"] for tach in taches) / len(taches) if taches else 0)
elif choix == "visualiseur":
    import streamlit as st
    import pandas as pd
    @st.cache_data
    def charger_donnees():
        return pd.read_csv("data.csv")

    df = charger_donnees()
    st.title("Visualisateur de donnees")
    categorie = st.sidebar.multiselect("Categories", df["categorie"].unique())
    if categorie:
        df = df[df["categorie"].isin(categorie)]
    st.dataframe(df)
    st.bar_chat(df, x="categorie", y="valeur")
elif choix == "rocial":
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