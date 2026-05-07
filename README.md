# Real-Time Data Pipeline Monitoring Dashboard

## Project Overview
This project simulates a real-world data pipeline system that:
- Processes data from CSV
- Generates logs (INFO, ERROR)
- Stores logs in JSON format
- Analyzes logs
- Displays insights using an interactive dashboard

## Tech Stack
- Python
- Pandas
- Streamlit
- Matplotlib
- Scikit-learn

## Workflow

1. Data Processing (`real_processor.py`)
2. Log Generation (`logs.json`)
3. Dashboard Visualization (`dashboard.py`)

## Features

- Real-time log monitoring
- Error detection
- Data validation (valid vs invalid)
- Interactive filters
- Charts (Bar + Pie)
- Processing insights

## Dataset
Custom dataset simulating real-world records:
1.Valid & Invalid entries
2.Categories
3.Status (active/failed)

## Run Locally


Step 1: Create environment
python -m venv venv

step 2: Activate
venv\Scripts\activate

Step 3: Install dependencies
pip install -r requirements.txt

## Note
The project initially started with a simulated monitoring system using `log_generator.py` to create random system logs and `log_analysis.py` to analyze those logs and detect anomalies. This was mainly used for testing, learning log analysis, and understanding monitoring workflows.

The project was later upgraded into a more realistic CSV-based data pipeline system using `realprocessor.py` and `dashboard.py`. In the updated version, the system processes real CSV data, validates records, generates structured logs, detects errors, and displays insights through an interactive dashboard with charts and analytics.

The newer pipeline is more effective because it works with actual dataset processing instead of randomly generated logs, making the monitoring, validation, and analysis more meaningful and closer to real-world data engineering workflows.

Step 4: Run data processor
python real_processor.py

Step 5: Run dashboard
streamlit run dashboard.py
