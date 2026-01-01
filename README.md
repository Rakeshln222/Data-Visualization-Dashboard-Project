# 🌍 COVID-19 Data Visualization Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

## ✨ Features

### 📊 **Interactive Visualizations**
- **Time Series Analysis**: Track case trends over time with interactive line charts
- **Geographical Distribution**: View case distribution on interactive maps
- **Comparative Analysis**: Compare countries with bar charts and pie charts
- **Growth Metrics**: Monitor daily growth rates and trends

### 🔧 **Advanced Filtering**
- Multi-country selection and comparison
- Custom date range filtering
- Multiple metric options (Confirmed, Deaths, Recovered, Active cases)
- Real-time data updates

### 📈 **Comprehensive Metrics**
- Key performance indicators (KPIs)
- Mortality and recovery rates
- Growth rate calculations
- Data quality validation

### 💾 **Data Management**
- Multiple data sources (Sample, Database, Real-time API)
- Data export capabilities (CSV, Excel)
- SQLite database integration
- Automated data updates

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/covid-dashboard.git
   cd covid-dashboard
   ```

2. **Create virtual environment** (Recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The dashboard will open automatically

## 📁 Project Structure

```
covid_dashboard/
│
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .streamlit/           # Streamlit configuration
│   └── config.toml
│
├── data/                 # Data directory
│   ├── raw/             # Raw data files
│   ├── processed/       # Processed data files
│   └── database/        # SQLite database files
│
├── src/                 # Source code modules
│   ├── __init__.py
│   ├── data_loader.py   # Data loading and processing
│   ├── visualizations.py # Chart creation functions
│   └── utils.py         # Utility functions
│
├── assets/              # Static assets
│   ├── style.css        # Custom CSS styles
│   └── images/          # Images and icons
│
└── tests/               # Test suite
    └── test_app.py
```

## 🛠️ Configuration

### Data Sources
The dashboard supports three data sources:

1. **Sample Data**: Generated synthetic data for demonstration
2. **Database**: SQLite database with persistent storage
3. **Real-time API**: Live data from public COVID-19 APIs

## 📊 Usage Guide

### 1. **Data Source Selection**
- Choose between Sample Data, Database, or Real-time API in the sidebar
- Sample data is perfect for testing and demonstration
- Real-time API provides live COVID-19 statistics

### 2. **Country Selection**
- Select multiple countries for comparison
- Use the multi-select dropdown in the sidebar
- Data automatically updates based on selection

### 3. **Date Range Filtering**
- Set custom date ranges for analysis
- Use the date picker in the sidebar
- View trends over specific time periods

### 4. **Metric Analysis**
- Choose from:
  - **Confirmed Cases**: Total positive cases
  - **Deaths**: Total fatalities
  - **Recovered**: Total recoveries
  - **Active Cases**: Current active infections

### 5. **Data Export**
- Download filtered data as CSV or Excel
- View raw data tables within the application
- Export specific visualizations as images

## 🎯 Key Features in Detail

### Interactive Charts
- **Hover Effects**: Get detailed information on hover
- **Zoom and Pan**: Interactive chart navigation
- **Dynamic Updates**: Real-time chart updates based on filters
- **Multiple Chart Types**: Line, bar, pie, scatter, and map visualizations

### Data Validation
- Automatic data quality checks
- Missing value detection
- Consistency validation across time periods
- Alert system for data issues

### Performance Optimization
- Data caching for faster load times
- Efficient data processing algorithms
- Lazy loading for large datasets
- Memory optimization techniques

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click

### Docker Deployment
```bash
# Build the image
docker build -t covid-dashboard .

# Run the container
docker run -p 8501:8501 covid-dashboard
```

### Heroku Deployment
```bash
# Create Heroku app
heroku create your-covid-dashboard

# Deploy
git push heroku main
```

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=src tests/

# Run specific test file
python -m pytest tests/test_app.py -v
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Write docstrings for all functions
- Include tests for new features


### Visualization Functions
```python
from src.visualizations import ChartBuilder

builder = ChartBuilder()
fig = builder.create_time_series(df, 'Confirmed', countries, 'Title')
fig = builder.create_geographical_map(df, 'Deaths')
```

## 🐛 Troubleshooting

### Common Issues

**ModuleNotFoundError**
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt
```

**Port already in use**
```bash
# Use different port
streamlit run app.py --server.port=8502
```

**Memory issues**
- Reduce the date range
- Select fewer countries
- Clear Streamlit cache

### Getting Help
- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Open an [issue](https://github.com/yourusername/covid-dashboard/issues)
- Check existing issues for solutions

## 📊 Data Sources

- **Sample Data**: Generated synthetic data mimicking real COVID-19 patterns
- **Real-time Data**: [disease.sh API](https://disease.sh/)
- **Historical Data**: JHU CSSE COVID-19 Data

## 🛡️ Privacy & Security

- No personal data is collected or stored
- All data is aggregated and anonymized
- Database is stored locally
- No tracking or analytics
