# 📊 Sensor Data Monitoring Dashboard

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Dash](https://img.shields.io/badge/dash-2.0.0%2B-brightgreen)

## Overview

The **Sensor Data Monitoring Dashboard** is a comprehensive visualization tool built using Dash and Plotly. It provides real-time monitoring, visualization of various sensor data including XYZ axis data, Mean Squared Error (MSE), Standard Deviation (STD), and Peak Frequency data, along with an alarm functionality for out-of-range sensor values.

## Features

- **XYZ Axis Data Visualization**
- **Mean Squared Error (MSE) Visualization**
- **Standard Deviation (STD) Visualization**
- **Peak Frequency Data Visualization**
- **3D Surface Plots**
- **Real-Time Data Monitoring**
- **Alarm Functionality**
- **Week Comparison Feature**

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/sensor-data-monitoring.git
   cd sensor-data-monitoring

2. **Create and activate a virtual environment:**

  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
  pip install -r requirements.txt

🚀 Usage
1. **Start the application:**
  python app.py
2. **Access the dashboard:**
  Open your web browser and go to http://127.0.0.1:8050/ to view the dashboard.

📁 Directory Structure
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

📦 Dependencies
Dash
Dash Bootstrap Components
Plotly
Pandas
NumPy
SciPy
SQLAlchemy
Cachetools
MySQL Connector

📊 Data Source
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
✨ Customization
Styling: Modify the static/style.css file to change the appearance of the dashboard.
Data Fetching: Update data.py to modify the data fetching logic or to connect to a different database.
🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

💬 Acknowledgements
Thanks to the Dash and Plotly teams for their excellent libraries.
Inspiration for this project came from various online resources and tutorials.
📧 Contact
For questions or feedback, please contact yourname.
