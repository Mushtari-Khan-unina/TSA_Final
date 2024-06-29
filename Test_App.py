import streamlit as st
import pandas as pd
import json

# Load the Jupyter notebook
notebook_path = "Day_Wise/Day_5 (2).ipynb"
with open(notebook_path, 'r') as file:
    notebook = json.load(file)

# Extract headings and corresponding cells
headings = [
    "Importing",
    "Libraries",
    "Dataset",
    "About Data",
    "Exploratory Data Analysis",
    "Candle Stick Charts",
    "Volume",
    "Returns",
    "Decomposition",
    "Stationarity Tests",
    "Transformation",
    "Auto ARIMA",
    "Fitting the Model",
    "TSForecastingExperiment",
    "Model comparision"
]

# Create a dictionary to store the content under each heading
content = {heading: [] for heading in headings}

current_heading = None
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        for line in cell['source']:
            if line.startswith('#'):
                heading = line.strip('#').strip()
                if heading in headings:
                    current_heading = heading
                break
    if current_heading:
        content[current_heading].append(cell)

# Streamlit App
st.sidebar.title("Time Series Analysis")
page = st.sidebar.radio("Navigation", headings)

# Function to display content for a selected page
def display_content(selected_heading):
    for cell in content[selected_heading]:
        if cell['cell_type'] == 'markdown':
            st.markdown(''.join(cell['source']))
        elif cell['cell_type'] == 'code':
            code = ''.join(cell['source'])
            st.code(code)
            try:
                exec(code, globals())
            except Exception as e:
                st.error(f"Error executing code: {e}")

# Display content based on the selected page
if page:
    st.title(page)
    display_content(page)
