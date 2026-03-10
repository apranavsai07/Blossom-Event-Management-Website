import streamlit as st
import requests

def show():
    st.header("🧑‍💼 Event Organiser Dashboard")
    
    st.subheader("Create New Event")
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    event_desc = st.text_area("Event Description")
    event_location = st.text_input("Event Location")
    event_id = st.text_input("Enter event ID")

    if st.button("Create Event"):
        if event_name and event_desc and event_location and event_id:
            event_data = {
                "name": event_name,
                "date": str(event_date),
                "desc": event_desc,
                "location": event_location,
                "id": event_id
            }
            try:
                response = requests.post("http://127.0.0.1:8000/create_event", json=event_data)
                if response.status_code == 200:
                    st.success(f"✅ Event '{event_name}' created for {event_date}")
                else:
                    st.error("❌ Failed to create event.")
            except Exception as e:
                st.error(f"🚫 Error connecting to backend: {e}")
        else:
            st.warning("Please fill all fields.")
    
    st.subheader("Edit Existing Event")
    edit_id = st.text_input("Enter Event ID to Edit")
    if st.button("Load Event"):
        st.info(f"Load and edit Event ID: {edit_id}")
