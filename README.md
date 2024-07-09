Sensor Data Monitoring Dashboard
Overview
This project is a comprehensive Sensor Data Monitoring Dashboard built using Dash and Plotly. The dashboard visualizes various sensor data including XYZ axis data, Mean Squared Error (MSE), Standard Deviation (STD), and Peak Frequency data. It also includes real-time data monitoring and alarm functionality for out-of-range sensor values.

Features
XYZ Axis Data Visualization: Displays time series data for X, Y, and Z axis.
Mean Squared Error (MSE) Visualization: Shows MSE data for X, Y, and Z axis.
Standard Deviation (STD) Visualization: Visualizes the standard deviation of X, Y, and Z axis data.
Peak Frequency Data Visualization: Plots the peak frequency data using bar charts.
3D Surface Plots: Provides 3D surface plots for XYZ axis, MSE, STD, and Peak Frequency data.
Real-Time Data Monitoring: Displays real-time sensor data and triggers alarms if values are out-of-range.
Week Comparison Feature: Allows users to compare data from different weeks side-by-side.

Installation
Clone the repository:
git clone https://github.com/yourusername/sensor-data-monitoring.git
cd sensor-data-monitoring
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
pip install -r requirements.txt

Usage
Start the application:
python app.py
Access the dashboard:
Open your web browser and go to http://127.0.0.1:8050/ to view the dashboard.

Directory Structure
sensor-data-monitoring/
│
├── app.py                    # Main application file
├── data.py                   # Data fetching and caching logic
├── layout.py                 # Layout and UI components
├── plots.py                  # Plotting functions
├── requirements.txt          # List of dependencies
├── static/
│   └── style.css             # Custom CSS for styling
└── README.md                 # Project documentation

Dependencies
Dash
Dash Bootstrap Components
Plotly
Pandas
NumPy
SciPy
SQLAlchemy
Cachetools
MySQL Connector
Data Source
The application fetches sensor data from a MySQL database. The database schema should include tables for AccelerometerData and StatisticsData with the following structure:

AccelerometerData
Column	Type
RECORDED_TIME	DATETIME
XOUT	FLOAT
YOUT	FLOAT
ZOUT	FLOAT
StatisticsData
Column	Type
RECORDED_TIME	DATETIME
MSE_X	FLOAT
MSE_Y	FLOAT
MSE_Z	FLOAT
STD_X	FLOAT
STD_Y	FLOAT
STD_Z	FLOAT
PEAK_FREQ_X	FLOAT
PEAK_FREQ_Y	FLOAT
PEAK_FREQ_Z	FLOAT

Customization
Styling: Modify the static/style.css file to change the appearance of the dashboard.
Data Fetching: Update data.py to modify the data fetching logic or to connect to a different database.

Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

Acknowledgements
Thanks to the Dash and Plotly teams for their excellent libraries.
Inspiration for this project came from various online resources and tutorials.
Contact
For questions or feedback, please contact yourname.
