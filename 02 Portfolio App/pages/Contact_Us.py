import streamlit as st

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email")
    message = st.text_area("Your message")
    button = st.form_submit_button("Send")
    if button:
        message = message + user_email
        print("I was pressed")


# 
