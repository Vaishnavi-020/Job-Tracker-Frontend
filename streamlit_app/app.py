import streamlit as st
from auth import login_page
st.set_page_config(page_title="Job Tracker",layout="wide")

login_page()
if st.session_state.get("login_success"):
    st.success("Logged in successfully")
    st.session_state["login_success"]=False