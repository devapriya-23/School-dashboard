import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="School Dashboard", layout="wide")

st.title("📊 School Management Analytics")

# Load data
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()   # remove spaces

# Sidebar filters
st.sidebar.header("Filter Options")

gender_options = df["gender"].unique()
topic_options = df["Topic"].unique()
class_options = df["Class"].unique()

selected_gender = st.sidebar.multiselect(
    "Select Gender", gender_options
)

selected_topic = st.sidebar.multiselect(
    "Select Topic", topic_options
)

selected_class = st.sidebar.multiselect(
    "Select Class", class_options
)

# Filtering logic
filtered_df = df.copy()

if selected_gender:
    filtered_df = filtered_df[filtered_df["gender"].isin(selected_gender)]

if selected_topic:
    filtered_df = filtered_df[filtered_df["Topic"].isin(selected_topic)]

if selected_class:
    filtered_df = filtered_df[filtered_df["Class"].isin(selected_class)]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(filtered_df))
col2.metric("Avg Raised Hands", round(filtered_df["raisedhands"].mean(), 2))
col3.metric("Avg Visited Resources", round(filtered_df["VisITedResources"].mean(), 2))

st.divider()

# Chart 1 - Participation by Class
st.subheader("Participation by Class")
fig1 = px.bar(
    filtered_df,
    x="Class",
    y="raisedhands",
    color="gender",
    title="Raised Hands by Class & Gender"
)
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 - Topic wise performance
st.subheader("Topic wise Performance")
fig2 = px.box(
    filtered_df,
    x="Topic",
    y="raisedhands",
    color="gender"
)
st.plotly_chart(fig2, use_container_width=True)

# Chart 3 - Parents satisfaction
st.subheader("Parents Satisfaction")
fig3 = px.histogram(
    filtered_df,
    x="ParentschoolSatisfaction",
    color="gender",
    barmode="group"
)
st.plotly_chart(fig3, use_container_width=True)

# Show data
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)
st.caption("Data Source: xAPI-Edu-Data")