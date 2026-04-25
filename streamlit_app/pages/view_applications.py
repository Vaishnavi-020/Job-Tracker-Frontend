import streamlit as st
from api import get_applications,update_application_status

def show(token):
    st.title("📄 Your Applications")

    apps = get_applications(token) 

    if not apps:
        st.warning("No applications found")
        return

    for app in apps:
        st.write(
            f"### {app.get('company_name', 'N/A')} - {app.get('role', 'N/A')}"
        )
        st.write(f"📅 Applied: {app.get('applied_date', 'N/A')}")
        st.write(f"Status: {app.get('status', 'N/A')}")

        new_status = st.selectbox(
            "Update Status",
            ["Applied", "Interview", "Rejected"],
            key=f"status_{app['id']}"
        )

        if st.button("Update", key=f"btn_{app['id']}"):
            response=update_application_status(token, app["id"], new_status)
            if response.status_code==200:   
                st.success("Updated!")
            else:
                st.error(f"Failed: {response.text}")

            st.success("Updated!")
            st.rerun()