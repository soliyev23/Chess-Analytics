# Chess Analytics Dashboard 🎮

## Overview
A Streamlit-based interactive dashboard for analyzing online chess game data. This application provides comprehensive visualizations and analysis tools for chess match statistics, including player ratings, game outcomes, and opening moves.

## Features
- **Data Overview**
  - Basic dataset statistics
  - Interactive data table view
  - Pie charts for rated games and winner distribution
  - Victory status analysis

- **Data Cleaning Tools**
  - Missing value detection and visualization
  - Automated ID generation for missing values
  - Multiple imputation methods (Mean, Median, Mode)
  - Duplicate handling

- **Advanced Analytics**
  - Time-series analysis of game distributions
  - Winner statistics visualization
  - Game duration analysis with customizable bins
  - Opening moves popularity charts
  - Player rating distribution analysis
  - Correlation heatmaps with selectable features

## Requirements
```
streamlit
pandas
matplotlib
seaborn
plotly.express
streamlit_option_menu
```

## Installation
1. Clone the repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Data Requirements
The application expects a CSV file named `chess_dataset.csv` with the following columns:
- id
- rated
- created_at
- winner
- victory_status
- increment_code
- white_id
- black_id
- white_rating
- black_rating
- moves
- opening_eco
- opening_name
- turns

## Usage
1. Place your `chess_dataset.csv` file in the project directory
2. Run the application:
```bash
streamlit run app.py
```

## Dashboard Sections

### 1. About DataFrame
- Overview of the chess dataset
- Basic statistics and distributions
- Interactive pie charts and bar graphs

### 2. Missing Value Analysis
- Comprehensive missing value detection
- Interactive data cleaning tools
- Multiple imputation strategies for different data types
- Before/after comparison statistics

### 3. Graphic Analysis
- Interactive time series visualizations
- Customizable histograms with color pickers
- Rating distribution comparisons
- Opening move analysis
- Correlation analysis with selectable features

## Customization
- Use the sidebar to navigate between different sections
- Adjust visualization parameters using interactive controls
- Customize bin sizes and colors for histograms
- Select specific features for correlation analysis

## Visual Features
- Snow animation effect
- Chess-themed sidebar image
- Celebration balloons on finish
- Interactive expandable sections
- Color-coded visualizations

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
