# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Page configuration
st.set_page_config(
    page_title="COVID-19 Dashboard",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🌍 COVID-19 Data Visualization Dashboard")
st.markdown("Interactive visualization of COVID-19 statistics worldwide")

# Sample data generation (replace with real data loading)
@st.cache_data
def load_data():
    # Generate sample COVID-19 data
    countries = ['USA', 'India', 'Brazil', 'Russia', 'UK', 'France', 'Germany', 'Japan', 'South Korea', 'Australia']
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    
    data = []
    for country in countries:
        base_cases = np.random.randint(1000, 10000)
        base_deaths = np.random.randint(10, 100)
        
        for date in dates:
            # Simulate some trends
            trend = np.sin((date - dates[0]).days / 30) * 0.5 + 1
            cases = max(0, int(base_cases * trend + np.random.normal(0, 100)))
            deaths = max(0, int(base_deaths * trend + np.random.normal(0, 10)))
            recovered = int(cases * 0.8 + np.random.normal(0, 50))
            
            data.append({
                'Country': country,
                'Date': date,
                'Confirmed': cases,
                'Deaths': deaths,
                'Recovered': recovered,
                'Active': cases - deaths - recovered
            })
    
    return pd.DataFrame(data)

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("🔧 Filters")

# Country multiselect
countries = st.sidebar.multiselect(
    "Select Countries:",
    options=df['Country'].unique(),
    default=df['Country'].unique()[:3]
)

# Date range selector
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Metric selector
metric = st.sidebar.selectbox(
    "Select Metric:",
    options=['Confirmed', 'Deaths', 'Recovered', 'Active']
)

# Filter data based on selections
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = df[
        (df['Country'].isin(countries)) & 
        (df['Date'] >= pd.to_datetime(start_date)) & 
        (df['Date'] <= pd.to_datetime(end_date))
    ]
else:
    filtered_df = df[df['Country'].isin(countries)]

# Main dashboard layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Time Series Analysis")
    
    # Time series chart
    if not filtered_df.empty:
        fig_time = px.line(
            filtered_df, 
            x='Date', 
            y=metric, 
            color='Country',
            title=f'{metric} Cases Over Time'
        )
        st.plotly_chart(fig_time, use_container_width=True)

with col2:
    st.subheader("🗺️ Geographical Distribution")
    
    # Create a summary for map (using mock coordinates)
    summary_df = filtered_df.groupby('Country')[metric].max().reset_index()
    
    # Mock coordinates for demonstration
    coords = {
        'USA': [37.0902, -95.7129],
        'India': [20.5937, 78.9629],
        'Brazil': [-14.2350, -51.9253],
        'Russia': [61.5240, 105.3188],
        'UK': [55.3781, -3.4360],
        'France': [46.6034, 1.8883],
        'Germany': [51.1657, 10.4515],
        'Japan': [36.2048, 138.2529],
        'South Korea': [35.9078, 127.7669],
        'Australia': [-25.2744, 133.7751]
    }
    
    summary_df['Lat'] = summary_df['Country'].map(lambda x: coords[x][0])
    summary_df['Lon'] = summary_df['Country'].map(lambda x: coords[x][1])
    
    fig_map = px.scatter_geo(
        summary_df,
        lat='Lat',
        lon='Lon',
        size=metric,
        color='Country',
        hover_name='Country',
        size_max=50,
        title=f'{metric} Cases by Country'
    )
    st.plotly_chart(fig_map, use_container_width=True)

# Second row of charts
col3, col4 = st.columns(2)

with col3:
    st.subheader("📊 Current Statistics")
    
    # Latest data bar chart
    latest_data = filtered_df[filtered_df['Date'] == filtered_df['Date'].max()]
    
    fig_bar = px.bar(
        latest_data,
        x='Country',
        y=metric,
        color='Country',
        title=f'Current {metric} Cases by Country'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col4:
    st.subheader("📈 Growth Rate")
    
    # Calculate growth rates
    growth_data = []
    for country in countries:
        country_data = filtered_df[filtered_df['Country'] == country].sort_values('Date')
        if len(country_data) > 1:
            latest = country_data[metric].iloc[-1]
            previous = country_data[metric].iloc[-2]
            growth_rate = ((latest - previous) / previous * 100) if previous > 0 else 0
            growth_data.append({'Country': country, 'Growth_Rate': growth_rate})
    
    if growth_data:
        growth_df = pd.DataFrame(growth_data)
        fig_growth = px.bar(
            growth_df,
            x='Country',
            y='Growth_Rate',
            color='Growth_Rate',
            color_continuous_scale='RdYlGn',
            title='Daily Growth Rate (%)'
        )
        st.plotly_chart(fig_growth, use_container_width=True)

# Key metrics at the bottom
st.subheader("📋 Key Metrics")

# Calculate summary statistics
total_confirmed = filtered_df[filtered_df['Date'] == filtered_df['Date'].max()]['Confirmed'].sum()
total_deaths = filtered_df[filtered_df['Date'] == filtered_df['Date'].max()]['Deaths'].sum()
total_recovered = filtered_df[filtered_df['Date'] == filtered_df['Date'].max()]['Recovered'].sum()

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric("Total Confirmed", f"{total_confirmed:,}")

with metric2:
    st.metric("Total Deaths", f"{total_deaths:,}")

with metric3:
    st.metric("Total Recovered", f"{total_recovered:,}")

with metric4:
    mortality_rate = (total_deaths / total_confirmed * 100) if total_confirmed > 0 else 0
    st.metric("Mortality Rate", f"{mortality_rate:.2f}%")

# Data table
with st.expander("View Raw Data"):
    st.dataframe(filtered_df.sort_values(['Country', 'Date']))

# Add some custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    # This is already running in Streamlit
    pass