# We can run the streamlit application by typing the following command in terminal: `streamlit run ./main.py`
# It will then run a webserver for us on the port no 8501
# Anytime something must be updated on the screen, Streamlit reruns the entire Python script from top to bottom
import streamlit as st

pressed = st.button("Press me")
print("First:", pressed)

pressed = st.button("Second button")
print("Second:", pressed)
