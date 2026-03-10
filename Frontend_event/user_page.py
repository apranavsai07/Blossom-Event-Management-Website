import streamlit as st
import requests

def show():
    st.header("👤 User Dashboard")

    # 1. Fetch Events
    events = []
    try:
        response = requests.get("http://127.0.0.1:8000/events")
        if response.status_code == 200:
            events = response.json()
        else:
            st.error("❌ Failed to fetch events.")
    except Exception as e:
        st.error(f"🚫 Error connecting to backend: {e}")

    # 2. Display Events
    st.subheader("📅 Browse Available Events")
    if events:
        for event in events:
            with st.expander(f"{event['name']} ({event['date']}) - {event['location']}"):
                st.markdown(f"**Event ID:** {event.get('id', 'N/A')}")
                st.markdown(f"**Description:** {event['desc']}")
    else:
        st.info("No events available.")

    # 3. Register New User
    st.header("📝 Register New User")

    name = st.text_input("Full Name", key="user_name")
    email = st.text_input("Email", key="user_email")
    password = st.text_input("Password", type="password", key="user_password")

    if st.button("Register User", key="user_register_button"):
        if name and email and password:
            payload = {
                "name": name,
                "email": email,
                "password": password
            }
            try:
                res = requests.post("http://127.0.0.1:8000/register_user", json=payload)
                data = res.json()
                if "message" in data:
                    st.success("✅ " + data["message"])
                else:
                    st.error("❌ " + data.get("error", "Unknown error"))
            except Exception as e:
                st.error(f"🚫 Backend error: {e}")
        else:
            st.warning("Please fill all fields.")

    # 4. Register for Event
    st.subheader("📝 Register for Event")
    event_id = st.text_input("Enter Event ID", key="event_id_input")
    event_email = st.text_input("Your Email", key="event_email_input")

    if st.button("Register for Event", key="register_event_button"):
        if event_id and event_email:
            payload = {
                "email": event_email,
                "event_id": event_id
            }
            try:
                res = requests.post("http://127.0.0.1:8000/register_event", json=payload)
                data = res.json()
                if "message" in data:
                    st.success("✅ " + data["message"])
                else:
                    st.error("❌ " + data.get("error", "Unknown error"))
            except Exception as e:
                st.error(f"🚫 Backend error: {e}")
        else:
            st.warning("Please provide both event ID and your email.")

    # 5. Payment (mocked)
    st.subheader("💳 Make Payment")
    payment = st.text_input("Payment Details (e.g., Card Number)", key="payment_input")
    if st.button("Pay Now", key="payment_button"):
        if payment:
            st.success("✅ Payment Successful (Mocked)")
        else:
            st.warning("Please enter payment details.")
