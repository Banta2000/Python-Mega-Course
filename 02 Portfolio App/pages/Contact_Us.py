import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email")
    topic = st.selectbox("What topic do you want to discuss?", ("General Inquiry", "Support", "Feedback", "Other"))
    raw_message = st.text_area("Your message")
    
    # Format the email message
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
Topic: {topic}
{raw_message}
    """
    
    
    button = st.form_submit_button("Send")
    if button:
        send_email(message)
        st.info("Email sent successfully")
