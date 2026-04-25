import streamlit as st
from auth import login_page,signup_page
from pages import dashboard,add_application,view_applications

st.set_page_config(page_title="Job Tracker",layout="wide")

if "token" not in st.session_state:
    st.session_state["token"]=None

if not st.session_state["token"]:
    option=st.sidebar.radio("Select",["Login","Signup"])

    if option=="Login":
        login_page()
        if st.session_state.get("login_success"):
            st.success("Logged in successfully")
            st.session_state["login_success"]=False
    else:
        signup_page()
        if st.session_state.get("signup_success"):
            st.success("Signup Successfull!")
            st.session_state["signup_success"]=False

else:
    st.sidebar.title("Navigation")
    page=st.sidebar.radio("Go to",
                          ["Dashboard","Add Application","View Applications"])

    if page=="Dashboard":
        dashboard.show()
    elif page=="Add Application":
        add_application.show(st.session_state["token"])
    elif page=="View Applications":
        view_applications.show(st.session_state["token"])

