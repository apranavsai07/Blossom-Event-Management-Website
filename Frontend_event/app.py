import streamlit as st

st.set_page_config(page_title="Blossom", layout="wide")

st.title("Blossom: Making Your Event Unforgettable")  # Move this to the top

# then load pages
import user_page
import organiser_page
import admin_page

role = st.sidebar.selectbox("Select Your Role", ["User", "Organiser", "Admin"])
if role == "User":
    user_page.show()
elif role == "Organiser":
    organiser_page.show()
elif role == "Admin":
    admin_page.show()


    #page = st.sidebar.selectbox("Navigate", ["Register"])
    #if page == "Register":
   # register_page.show()



# In your navigation menu:



