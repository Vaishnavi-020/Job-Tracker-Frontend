import streamlit as st
from auth import login_page,signup_page
st.set_page_config(page_title="Job Tracker",layout="wide")

signup_page()
if st.session_state.get("signup_success"):
    st.success("Signup Successfull!")
    st.session_state["signup_success"]=False

login_page()
if st.session_state.get("login_success"):
    st.success("Logged in successfully")
    st.session_state["login_success"]=False