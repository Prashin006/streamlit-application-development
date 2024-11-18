import streamlit as st
from datetime import datetime

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

st.title("user information form".capitalize())

# key is used to uniquely identify the form
# Only after the submit button is pressed, the code reruns and updates the state
with st.form(key="user_info_form", clear_on_submit=True):
    name1 = st.text_input("Enter your first name")
    birth_date = st.date_input(
        "Enter your birth date", min_value=min_date, max_value=max_date
    )

    if birth_date:
        age = max_date.year - birth_date.year
        if (birth_date.month > max_date.month) or (
            birth_date.month == max_date.month and birth_date.day > max_date.day
        ):
            age -= 1
        st.write(f"Your calculated age is {age} years!")

    submit_button1 = st.form_submit_button(label="Submit Form")

    if submit_button1:
        if not name1 or not birth_date:
            st.warning("Please fill out all of the form fields!")
        else:
            st.success(f"Thank you, {name1}. You age is {age}.")
            st.balloons()
