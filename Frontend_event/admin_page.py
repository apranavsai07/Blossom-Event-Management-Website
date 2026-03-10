import streamlit as st

def show():
    st.header("🔐 Admin Panel")
    
    st.subheader("Generate Reports")
    if st.button("Download Event Reports"):
        st.success("Report downloaded!")
    
    st.subheader("Manage Users")
    if st.button("View All Users"):
        st.info("Displaying all users... (placeholder)")
    
    st.subheader("Send Notifications")
    message = st.text_area("Enter Notification Message")
    if st.button("Send Notification"):
        st.success("Notification sent!")
