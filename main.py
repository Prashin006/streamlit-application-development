import streamlit as st
import pandas as pd

# Title
st.title("Form Elements")

# Form to hold interactive elements
with st.form(key="sample_form", clear_on_submit=True):
    # Text input
    st.subheader("Text Input")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")

    # Date and time inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Select your preferred time")

    # Selectors 
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["Fried Rice", "Noodles", "Soup"])
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])

    # Toggles and checkboxes
    st.subheader("Toggles & Checkboxes")
    notifications = st.checkbox("Receive notifications?", value=True)
    toggle_value = st.checkbox("Enable dark mode?", value=False)

    # Submit button for the form
    submit_button = st.form_submit_button(label="Submit")

# Outside of the form
st.subheader("Buttons")