import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_values = {"name": None, "height": None, "gender": None, "dob": None}

with st.form(key="user_info_form", clear_on_submit=True):
    form_values["name"] = st.text_input("Enter your name")
    form_values["height"] = st.number_input(
        "Enter your height (cms)", step=1, min_value=0, max_value=250
    )
    form_values["gender"] = st.selectbox(
        "Select your gender", ["Male", "Female", "Other"]
    )
    form_values["dob"] = st.date_input(
        "Enter your date of birth",
        min_value=datetime(1940, 1, 1),
        max_value=datetime.now(),
    )

    submit_button = st.form_submit_button(label="Submit")
    print("after submit")
    if submit_button:
        print("in if")
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Information")
            for key, val in form_values.items():
                st.write(f"{key.capitalize()}: {val}")
