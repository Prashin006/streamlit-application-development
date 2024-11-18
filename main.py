import streamlit as st

# A simple counter variable without session state
counter = 0

st.write(f"Counter value: {counter}")

# Button to increment the counter
if st.button("Increment Counter"):
    counter += 1
    st.write(f"Counter incremented to {counter}")
else:
    st.write(f"Counter stays at {counter}")

# Explanation
# After pressing the increment button every time, the counter stays at 1 and does not move forward. This is because when we press the button, the code reruns from the start and `counter = 0` line is at the top, so counter becomes 0 every time we press the button.
# `st.write(f"Counter value: {counter}")` line writes the value `0` of the counter and
# then the button value is evaluated to True and counter is incremented from 0 to 1 and the value 1 is written on the screen.
