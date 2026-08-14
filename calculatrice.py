import streamlit as st

st.set_page_config(page_title="Calculatrice" , page_icon="🧮" , layout="wide" )
if "calcul" not in st.session_state:
        st.session_state.calcul = ""
st.title("CALCULATRICE")
st.text_input("Ecran", st.session_state.calcul, disabled=True)
def bouton(valeur):
        st.sesion_state.calcul += valeur 
coln1,coln2,coln3,coln4 =st.columns(4)
with coln1:
        if st.button("7"):bouton("7")
        if st.button("4"):bouton("4")
        if st.button("1"):bouton("1")
        if st.button("0"):bouton("0")
with coln2:
        if st.button("8"):bouton("8")
        if st.button("5"):bouton("5")
        if st.button("2"):bouton("2")
        if st.button("."):bouton(".")
with coln3:
        if st.button("9"):bouton("9")
        if st.button("6"):bouton("6")
        if st.button("3"):bouton("3")
        if st.button("+"):bouton("+")
with coln4:
        if st.button("/"):bouton("/")
        if st.button("*"):bouton("*")
        if st.button("-"):bouton("-")
        if st.button("4"):
                try:
                        resultat = eval(st.session_state.calcul)
                        st.session_state.calcul = str(resultat)
                        st.rerun()
                except:
                        st.session_state.calcul = "Erreur"
                        st.rerun()
if st.button("AC"):
        st.session_state.calcul = ""
        st.rerun()
st.subheader("fonctions scientifiques")
c1,c2,c3,c4,c5 = st.columns(5)
with c1:
        if st.button():
                s