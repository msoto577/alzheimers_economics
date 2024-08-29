import streamlit as st
import streamlit_extras.switch_page_button  # For page navigation


# Title and Description
st.title("Economic Evaluations of Alzheimer's Disease")
st.write("""
    Economic evaluations are critical tools in healthcare decision-making, providing insights into the value and affordability of interventions. Two common types of economic evaluations are Cost-Effectiveness Analysis (CEA) and Budget Impact Analysis (BIA).

    **Cost-Effectiveness Analysis (CEA):** This type of study compares the relative costs and outcomes (effects) of two or more interventions. The goal is to determine which intervention provides the best outcome for the cost. It often results in a cost-effectiveness ratio, such as cost per quality-adjusted life year (QALY) gained.

    **Budget Impact Analysis (BIA):** BIA estimates the financial impact of adopting a new health intervention within a specific budget context. It helps policymakers understand the short- and long-term financial consequences of adopting a new therapy or intervention, considering the available resources.
    """)

# Buttons for each analysis
#st.write("## Select the type of analysis to perform:")
col1, col2 = st.columns(2)

with col1:
    cea_clicked = st.button("Cost-Effectiveness Analysis")

with col2:
    bia_clicked = st.button("Budget Impact Analysis")

# Analysis output section - full width
if cea_clicked:
    # Run the CEA model and display results
    streamlit_extras.switch_page_button.switch_page("Cost-Effectiveness Analysis")

if bia_clicked:
    st.write("## Budget Impact Analysis Results")
    # Run the BIA model and display results
    streamlit_extras.switch_page_button.switch_page("Budget Impact Analysis")