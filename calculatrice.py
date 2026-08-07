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
        