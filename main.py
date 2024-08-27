import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Natural History", "Simulation Model", "Results", "Publications"])

if page == "Home":
    st.title("Welcome to the Economic Evaluation of Alzheimer's Disease")
    st.write("Overview of the disease and its economic impact.")

elif page == "Natural History":
    st.title("Natural History of Alzheimer's Disease")
    st.write("Information about the progression of Alzheimer's Disease.")

elif page == "Simulation Model":
    st.title("Simulation Model")
    st.write("Details of the simulation model used.")

elif page == "Results":
    st.title("Results")
    st.write("Results of the simulation model.")

elif page == "Publications":
    st.title("Publications")
    st.write("List of publications relevant to Alzheimer's disease.")
