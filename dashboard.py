import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🎬 Netflix Data + Pipeline Monitoring Dashboard")

# ---------------------------
# LOAD CSV DATA
# ---------------------------
df_data = pd.read_csv("data.csv")

# ---------------------------
# CLEAN DATA
# ---------------------------
valid_df = df_data[
    (df_data["title"] != "INVALID") &
    (df_data["genre"] != "INVALID")
]

invalid_df = df_data[~df_data.index.isin(valid_df.index)]

# ---------------------------
# LOAD LOGS
# ---------------------------
logs = []
with open("logs.json") as f:
    for line in f:
        logs.append(json.loads(line))

df_logs = pd.DataFrame(logs)
pipeline_logs = df_logs[df_logs["service"] == "data_pipeline"]

# ---------------------------
# KPIs
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(df_data))
col2.metric("Valid Records", len(valid_df))
col3.metric("Invalid Records", len(invalid_df))
col4.metric("Errors (Logs)", len(pipeline_logs[pipeline_logs["status"]=="ERROR"]))

st.divider()

# ---------------------------
# ROW 1 (CHARTS)
# ---------------------------
col1, col2 = st.columns(2)

# VALID vs INVALID
with col1:
    st.subheader("Valid vs Invalid")

    fig = px.pie(
        names=["Valid", "Invalid"],
        values=[len(valid_df), len(invalid_df)],
        color_discrete_sequence=["green", "red"]
    )
    st.plotly_chart(fig, use_container_width=True)

# ACTIVE vs FAILED
with col2:
    st.subheader("Active vs Failed")

    status_counts = df_data["status"].value_counts()

    fig = px.bar(
        x=status_counts.index,
        y=status_counts.values,
        color=status_counts.index,
        color_discrete_map={"active":"green","failed":"red"}
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------
# ROW 2 (CHARTS)
# ---------------------------
col1, col2 = st.columns(2)

# GENRE DISTRIBUTION
with col1:
    st.subheader("Genre Distribution")

    fig = px.pie(valid_df, names="genre")
    st.plotly_chart(fig, use_container_width=True)

# SUBSCRIPTION TYPE
with col2:
    st.subheader("Subscription Type")

    fig = px.bar(valid_df["subscription_type"].value_counts())
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------
# TABLES
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Invalid Records")
    st.dataframe(invalid_df)

with col2:
    st.subheader("Error Logs")
    st.dataframe(pipeline_logs[pipeline_logs["status"]=="ERROR"])

st.divider()

# ---------------------------
# PROCESS STEPS
# ---------------------------
st.subheader("Processing Steps")
st.dataframe(pipeline_logs[pipeline_logs["status"]=="INFO"])