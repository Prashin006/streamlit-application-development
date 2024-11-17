import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Data Elements")

# Dataframe section
st.subheader("Dataframe")
df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Chris", "Tim", "Prashin"],
        "Age": [34, 49, 44, 32, 21],
        "Occupation": [
            "Engineer",
            "Principal Staff",
            "Cricketer",
            "Engineer",
            "Cricketer",
        ],
    }
)

st.dataframe(df)


# Data editor section (Editable datafram)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)


# Static table section
st.subheader("Static Table")
st.table(df)


# Metrics section
st.subheader("Metrics")
st.metric(label="total rows", value=len(df))
st.metric(label="average age", value=round(editable_df["Age"].mean(), 2))
st.metric(label="max age", value=editable_df["Age"].max())
st.metric(label="min age", value=editable_df["Age"].min())


# json and dict section
st.subheader("JSON and Dictionary")
sample_dict = {
    "name": "Prashin",
    "age": 21,
    "skills": ["Python", "Data Science", "AI", "Machine Learning"],
}
st.json(sample_dict)

st.write("Dictionary View:", sample_dict)
