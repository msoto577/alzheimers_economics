import streamlit as st
from nbconvert import PythonExporter
import nbformat
import os
import requests

# Function to read and convert notebook to Python code
def run_notebook(notebook_path):
    if not os.path.isfile(notebook_path):
        st.error(f"The file {notebook_path} does not exist.")
        return ""
    
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    source, _ = exporter.from_notebook_node(notebook)
    return source

# Define the URL to your Jupyter notebook
url = "https://raw.githubusercontent.com/msoto577/alzheimers_economics/main/pages/IPECAD_CEA.ipynb"

# Fetch the notebook file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a temporary file
    notebook_path = "IPECAD_CEA.ipynb"
    with open(notebook_path, "wb") as f:
        f.write(response.content)

    # Convert notebook code
    notebook_code = run_notebook(notebook_path)

    # Execute the notebook code
    exec(notebook_code, globals())

    # Optionally, clean up the temporary file
    os.remove(notebook_path)
else:
    st.error("Failed to fetch the notebook file. Please check the URL or try again later.")

# Streamlit app layout
st.title('Cost-Effectiveness Analysis')


# Streamlit app layout
st.title('Cost-Effectiveness Analysis for Alzheimer`s Disease App')

# Define user inputs
replications = st.slider('Number of Replications', min_value=1, max_value=100, value=2)
patients = st.slider('Number of Patients', min_value=1, max_value=100000, value=10)


if st.button('Run Simulation'):
    # Check if the function exists before calling it
    if 'main' in globals():
        results = main(replications, patients)
        
        # Aggregate survival times
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

        # Plot differences with RCEI and ellipse
        st.write('Differences with RCEI and Ellipse:')
        fig_rcei = plot_differences_with_rcei_and_ellipse(results)  # Get the RCEI figure
        st.pyplot(fig_rcei)  # Display the RCEI figure in Streamlit

        # Plot acceptability curve
        st.write('Acceptability Curve:')
        fig_acceptability, ax_acceptability = plt.subplots()
        acceptability_curve(results)
        st.pyplot(fig_acceptability)

    else:
        st.write('Function not found in the notebook code.')
