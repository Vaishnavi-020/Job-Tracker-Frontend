import streamlit as st
from api import add_application

def show(token):
    with st.form("Job Application"):
        st.title("Add Job Application")

        company=st.text_input("Company")
        role=st.text_input('Role')
        location=st.text_input('Location')
        applied_date=st.date_input("Applied Date")
        link=st.text_input("Link")
        status=st.selectbox("Status",
                             ["Applied","Interview","Rejected","Offer"],
                             index=0)
        source=st.text_input("Applied on")
        notes=st.text_input("Additional notes")

        if st.form_submit_button("Submit"):
            data={
                "company_name":company,
                "role":role,
                "location":location,
                "applied_date":applied_date.isoformat(),
                "link":link,
                "status":status,
                "source":source,
                "notes":notes
            }

            res=add_application(token,data)

            if res.status_code==200:
                st.success("Application added!")
            else:
                st.error("Something went wrong!")



