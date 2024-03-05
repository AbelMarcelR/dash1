import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Baca data
day_df = pd.read_csv("day.csv")

# Ubah tipe data kolom 'dateday' menjadi datetime
day_df['dateday'] = pd.to_datetime(day_df['dateday'])

# Pilih kolom yang diperlukan
day_df = day_df[['dateday', 'month', 'count']]

# Agregasi data per bulan
monthly_rent_df = day_df.groupby('month')['count'].sum().reset_index()

# Agregasi data per hari
daily_rent_df = day_df.groupby('dateday')['count'].sum().reset_index()

# Membuat Dashboard
st.title('Bike Rental Dashboard 🚲')

# Chart per bulan
st.subheader('Monthly Rentals')
plt.figure(figsize=(10, 6))
plt.bar(monthly_rent_df['month'], monthly_rent_df['count'])
plt.xlabel('Month')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)
st.pyplot()

# Chart per hari
st.subheader('Daily Rentals')
plt.figure(figsize=(10, 6))
plt.plot(daily_rent_df['dateday'], daily_rent_df['count'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)
st.pyplot()



