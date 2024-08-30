import streamlit as st
from nbconvert import PythonExporter
import nbformat
import os

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

# Define the path to your Jupyter notebook
notebook_path = 'C:/Users/msoto/simPy_Trials/IPECAD/PRUEBAS STREAMLIT/IPECAD_CEA'

# Convert notebook code
notebook_code = run_notebook(notebook_path)

# Print notebook code to Streamlit for debugging
#st.write("Extracted notebook code:")
#st.code(notebook_code, language='python')

# Execute the notebook code
exec(notebook_code, globals())

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
