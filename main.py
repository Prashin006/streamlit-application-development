import streamlit as st

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
