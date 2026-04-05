import streamlit as st
from api import login,signup

def login_page():
    with st.form("Login Page"):

        st.title("Login")

        email=st.text_input("Email")
        password=st.text_input("Password",type="password")

        if st.form_submit_button("Login"):
            res=login({"email":email,"password":password})

            if res.status_code==200:
                token=res.json()["access_token"]
                st.session_state["token"]=token
                st.session_state["login_success"]=True
                st.rerun()
            else:
                st.error("Invalid credentials")
