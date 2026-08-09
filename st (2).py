import streamlit as st
st.set_page_config(page_icon="😎", page_title="kog",layout= "wide")
st.title("hello, world")

but = st.button("button")
is_first = True
if "is_first" not in st.session_state:
    st.session_state.is_first = True
if but :
    if st.session_state.is_first:
        st.snow()
        st.session_state.is_first = False
    else :
        st.balloons()
        st.session_state.is_first = True    






    
    



