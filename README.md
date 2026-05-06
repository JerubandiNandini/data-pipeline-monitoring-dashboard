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

Step 4: Run data processor
python realprocessor.py

Step 5: Run dashboard
streamlit run dashboard.py
