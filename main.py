# Session state is something that we can use to store values within the same user session
# Session persists through the rerun of our code
# If the user refreshes or reloads the page then the session changes
import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
st.write(f"Counter value: {st.session_state.counter}")
