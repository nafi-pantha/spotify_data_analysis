import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import plotly.express as px

# Load the dataset into a pandas DataFrame (adjust the path accordingly)

column_names = ['track_uri',    'track_name',       'artist_uri',       'artist_name',          'album_uri',    'album_name',   'album_artist_uri', 'album_artist_name',    'album_release_date',   'album_image_url', 
                'disc_number',  'track_number',     'track_duration',   'track_preview_url',    'explicit',     'popularity',   'isrc',             'added_by',	            'added_at',	            'artist_genres', 
                'danceability', 'energy',           'key',              'loudness',             'mode',         'speechiness',  'acousticness',     'instrumentalness',     'liveness',	            'valence', 
                'tempo',	    'time_signature',   'album_genres',     'label',                'copyrights']  

spotify_data = pd.read_csv("/Users/nafiulhassan/Projects/spotify_data_analysis/top_10000_1960-now.csv", names=column_names, skiprows=[0])

# Convert the 'date' column to a datetime data type
spotify_data = spotify_data[pd.to_datetime(spotify_data['album_release_date'], errors='coerce').notna()]
spotify_data['album_release_date'] = pd.to_datetime(spotify_data['album_release_date'], format='%Y-%m-%d')
#spotify_data['album_release_date'] = pd.to_datetime(spotify_data['album_release_date'])

# Extract the year from the 'date' column and create a new column 'year'
spotify_data['year'] = spotify_data['album_release_date'].dt.year

# Print the first row of data
# first_row = spotify_data.iloc[0]
# print(first_row)

# Calculate the variable changes within each year group
#spotify_data['tempo_change'] = spotify_data.groupby('year')['tempo'].diff()
#spotify_data['danceability_change'] = spotify_data.groupby('year')['danceability'].diff()
#spotify_data['energy_change'] = spotify_data.groupby('year')['energy'].diff()

#print(spotify_data[['track_name', 'year', 'tempo', 'tempo_change']])

# Group the data by year and calculate the average variable changes for each year
average_tempo_by_year = spotify_data.groupby('year')[['tempo', 'danceability', 'energy']].mean().reset_index()

# Define the start year and end year for the plot
start_year = 1960
end_year = 2023

# y Variables for titles
y_param_1 = 'Danceability'
y_param_2 = 'Energy'

# Filter the data for the specified years
filtered_data = average_tempo_by_year[(average_tempo_by_year['year'] >= start_year) & (average_tempo_by_year['year'] <= end_year)]

# Create a range of years with intervals of 5 years
#years_range = range(start_year, end_year + 1, 5)

# Chart Plot in Streamlit
st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 1, 1], gap="medium")
with col1:
    fig = px.area(filtered_data, x='year', y=['danceability', 'energy'], title=f'{y_param_1} and {y_param_2} from {start_year} to {end_year}')
    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("Analysis"):
        st.write("Here is the analysis!")

with col2:
    fig2 = px.line(filtered_data, x='year', y=['danceability', 'energy'], title=f'{y_param_1} and {y_param_2} from {start_year} to {end_year}')
    st.plotly_chart(fig2, use_container_width=True)
    with st.expander("Analysis"):
        st.write("Here is the analysis!")

with col3:
    fig2 = px.line(filtered_data, x='year', y='tempo', title=f'Tempo changes from {start_year} to {end_year}')
    st.plotly_chart(fig2, use_container_width=True)
    with st.expander("Analysis"):
        st.write("Here is the analysis!")

