import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Sales Dashboard")
st.write("This dashboard helps with sales")

data = {
  'Year': [2010, 2011, 2012, 2013, 2014, 2015],
  'Region': ['North', 'South','East', 'West', 'Central', 'North'],
  'Sales Account': [200, 210, 220, 230, 240, 250]
}
df = pd.DataFram(data)

selected_year = st.slider('Select a year', min_value=2010, max_value =2015, value =2013)

st.write(f"Data for the year {selected_year}:"}
filtereddf = df[df['Year'] == selected_year]
st.write(filtered_df)


fig, ax = plt.subplots()
ax.bar(filtered_df['Region'], filtered_df['Sales Amount'], color='skyblue')
plt.title(f'Sales in {selected_year}')
plt.xlabel()
plt.ylabel()
