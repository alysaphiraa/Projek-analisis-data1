# import sys
# print(sys.executable)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import streamlit as st

#Set style seaborn
sns.set(style='dark')

# # Menyiapkan data day_df
day_df = pd.read_csv("https://raw.githubusercontent.com/alysaphiraa/Projek-analisis-data1/refs/heads/main/Dashboard/main_data.csv")
day_df.head()



# Mengubah nama judul kolom
day_df.rename(columns={
    'weathersit': 'weather_labels',
    'season' : 'season_labels'
}, inplace=True)

# Mengubah angka menjadi keterangan
day_df['season_labels'] = day_df['season_labels'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

day_df['weather_labels'] = day_df['weather_labels'].map({
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
})


# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dteday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df
# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dteday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dteday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season_labels')[['registered', 'casual']].sum().reset_index()
    return season_rent_df
min_date = pd.to_datetime(day_df['dteday']).dt.date.min()
max_date = pd.to_datetime(day_df['dteday']).dt.date.max()
 

