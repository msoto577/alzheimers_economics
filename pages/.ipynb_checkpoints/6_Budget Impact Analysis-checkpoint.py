import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already defined these functions in the notebook:
# run_bia_simulation, calculate_confidence_intervals, plot_costs_with_ci

# Function to simulate and process results
def run_simulation_bia(num_patients, num_replications, follow_up_years):
    # Placeholder for the actual simulation function from the notebook
    # You would bring in the actual simulation logic from IPECAD_BIA.ipynb
    return run_bia_simulation(num_patients, num_replications, follow_up_years)

# Streamlit app layout
st.title("Budget Impact Analysis Simulation")

# User inputs
num_patients = st.number_input("Number of Patients:", min_value=1, value=100)
num_replications = st.number_input("Number of Replications:", min_value=1, value=1000)
follow_up_years = st.number_input("Follow-up Years:", min_value=1, value=10)

if st.button('Run Simulation'):
    # Run the simulation with user inputs
    results = run_simulation_bia(num_patients, num_replications, follow_up_years)
    
    # Assuming `results` contains the necessary data for further processing
    # Example: Breakdown of patients by stage for each year with CI

    # a) Table with number of patients by stage and group (control, intervention)
    st.write("Number of Patients by Stage and Group (with CI):")
    
    # Placeholder: Convert results into a pandas dataframe
    patients_df = pd.DataFrame({
        'Year': np.arange(1, follow_up_years + 1),
        'MCI (Control)': results['mci_control'],  # Assuming this structure
        'MCI (Intervention)': results['mci_intervention'],
        'Mild AD (Control)': results['mild_ad_control'],
        'Mild AD (Intervention)': results['mild_ad_intervention'],
        # Add other stages here
    })
    
    st.dataframe(patients_df)  # Display table
    
    # b) Table with total costs per group (control and intervention)
    st.write("Total Costs per Group (with CI):")
    
    costs_df = pd.DataFrame({
        'Year': np.arange(1, follow_up_years + 1),
        'Total Costs (Control)': results['total_costs_control'],
        'Total Costs (Intervention)': results['total_costs_intervention'],
        'CI Low (Control)': results['ci_low_control'],
        'CI High (Control)': results['ci_high_control'],
        # Add CI for intervention
    })
    
    st.dataframe(costs_df)  # Display table
    
    # c) Graph with total costs per group (control and intervention) with CI
    st.write("Total Costs per Group (with CI):")
    fig, ax = plt.subplots()
    
    ax.plot(costs_df['Year'], costs_df['Total Costs (Control)'], label="Control", color='blue')
    ax.fill_between(costs_df['Year'], costs_df['CI Low (Control)'], costs_df['CI High (Control)'], color='blue', alpha=0.2)
    
    ax.plot(costs_df['Year'], costs_df['Total Costs (Intervention)'], label="Intervention", color='red')
    ax.fill_between(costs_df['Year'], costs_df['CI Low (Control)'], costs_df['CI High (Control)'], color='red', alpha=0.2)
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Costs (€)')
    ax.set_title('Total Costs per Group with Confidence Intervals')
    ax.legend()
    
    st.pyplot(fig)  # Display the plot
