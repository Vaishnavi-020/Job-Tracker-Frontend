import streamlit as st
from api import login,signup

def signup_page():
    with st.form("Signup Page"):
        st.title("Signup")

        name=st.text_input("Username")
        email=st.text_input("Email")
        passwrod=st.text_input("Password",type="password")

        if st.form_submit_button("Signup"):
            res=signup({"name":name,"email":email,"password":passwrod})

            if res.status_code==200:
                token=res.json()["access_token"]
                st.session_state["token"]=token
                st.session_state["signup_success"]=True
                st.rerun
            else: 
                st.error("Something went wrong! Signup failed")

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