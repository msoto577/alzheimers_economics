import streamlit as st
import requests
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from io import StringIO
from IPython import get_ipython
import sys

# Function to fetch notebook from GitHub
def fetch_notebook_from_github(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch notebook: {e}")
        return None

# Function to execute notebook cells using IPython and nbformat
def execute_notebook(notebook_content):
    notebook = nbformat.reads(notebook_content, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    
    # Execute notebook in an isolated environment
    try:
        # Create a new IPython instance (or use existing one)
        ipython = get_ipython() if get_ipython() else IPython.get_ipython()
        
        # Redirect stdout to capture the output
        stdout_backup = sys.stdout
        sys.stdout = StringIO()
        
        ep.preprocess(notebook, {'metadata': {'path': './'}})
        sys.stdout.seek(0)
        execution_output = sys.stdout.read()  # Get the output
        sys.stdout = stdout_backup  # Restore stdout
        
        return execution_output

    except Exception as e:
        st.error(f"Error executing the notebook: {e}")
        return None

# Define the GitHub URL of your notebook (raw URL)
notebook_url = 'https://raw.githubusercontent.com/msoto577/alzheimers_economics/main/pages/IPECAD_BIA.ipynb'

# Fetch and execute the notebook
notebook_content = fetch_notebook_from_github(notebook_url)
if notebook_content:
    execution_output = execute_notebook(notebook_content)
    if execution_output:
        st.text("Notebook execution output:")
        st.code(execution_output)

# Streamlit app layout (as in the previous code)
st.title('Cost-Effectiveness Analysis for Alzheimer`s Disease App')

# Define user inputs
replications = st.slider('Number of Replications', min_value=1, max_value=100, value=2)
patients = st.slider('Number of Patients', min_value=1, max_value=100000, value=10)

if st.button('Run Simulation'):
    # If 'main' function was defined in the notebook, call it with parameters
    if 'main' in globals():
        results = main(replications, patients)
        
        # Assuming `aggregate_survival_times_by_stage` and other functions are also defined
        control_survival_times, intervention_survival_times = aggregate_survival_times_by_stage(results)
        
        # Create and display the survival summary table
        summary_df = create_survival_summary_table(control_survival_times, intervention_survival_times)
        st.write('Survival Summary Table:')
        st.dataframe(summary_df)
        
        # Plot survival curves with confidence intervals
        st.write('Survival Curves with Confidence Intervals:')
        fig_survival, ax_survival = plt.subplots()
        plot_survival_curve_with_confidence_intervals(control_survival_times, intervention_survival_times)
        st.pyplot(fig_survival)
