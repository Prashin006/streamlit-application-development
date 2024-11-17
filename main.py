import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Streamlit Charts Demo")

# Generate sample data
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])


# Area chart section
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar chart section
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line chart section
st.subheader("Line Chart")
st.line_chart(chart_data)

# Scatter plot/chart section
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({"x": np.random.randn(100), "y": np.random.randn(100)})
st.scatter_chart(scatter_data)

# Map section (displaying random sections on a map)
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50]
    + [37.76, -122.4],  # coordinates around san francisco
    columns=["lat", "lon"],
)
st.map(map_data)

# Pyplot section
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data["A"], label="A")
ax.plot(chart_data["B"], label="B")
ax.plot(chart_data["C"], label="C")
ax.set_title("Pyplot line chart")
ax.legend()
st.pyplot(fig)
