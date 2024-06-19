import pandas as pd
import streamlit as st

# Load data
file_path = "membership_records_100.xlsx"
df = pd.read_excel(file_path)

# Title
st.title("Membership Records Analysis")

# Show data
st.header("Membership Data")
st.write(df)

# Summary statistics
st.header("Summary Statistics")
st.write(df.describe())

# Analysis: Number of members by membership type
st.header("Number of Members by Membership Type")
membership_type_counts = df['Membership Type'].value_counts()
st.bar_chart(membership_type_counts)

# Analysis: Distribution of members by gender
st.header("Distribution of Members by Gender")
gender_counts = df['Gender'].value_counts()
st.bar_chart(gender_counts)

# Analysis: Average join date by membership type
st.header("Average Join Date by Membership Type")
df['Join Date'] = pd.to_datetime(df['Join Date'])
avg_join_date = df.groupby('Membership Type')['Join Date'].mean()
st.write(avg_join_date)

# Additional insights
st.header("Additional Insights")
st.write("You can add more analysis and visualizations here.")

# Run Streamlit app
# Use the following command to run the app:
# streamlit run dashboard.py
