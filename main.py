import streamlit as st
import os

st.title("Super Simple Title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is a ***Markdown***")
st.markdown("This is ~crossed~")

st.divider()
st.caption("This is a small caption")

code_example = """
def greet(name):
  print('Hello', name)
"""
st.code(code_example, language="python")

# For rendering images, we need to have those images in a folder named `static` located in the same directory as our main app file
# getcwd means get current working directory
st.image(os.path.join(os.getcwd(), "static", "bg.webp"))
