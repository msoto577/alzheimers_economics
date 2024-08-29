import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Natural History", "Simulation Conceptual Model", "Run Economic Evaluation" ,"Results", "Publications"])

if page == "Home":
    st.title("Economic Evaluation of Alzheimer's Disease")
    st.write("""
    Alzheimer's Disease (AD) is a progressive neurodegenerative disorder that predominantly affects older adults, leading to a gradual decline in cognitive functions such as memory, thinking, and behavior. It is the most common cause of dementia, accounting for 60-70% of all dementia cases worldwide. The pathological hallmark of Alzheimer's Disease is the accumulation of amyloid-beta plaques and neurofibrillary tangles composed of tau proteins in the brain. These abnormalities lead to widespread neuronal damage, brain atrophy, and eventually, the death of brain cells, which severely impacts the brain's ability to function.

    The initial symptoms of Alzheimer's Disease often include memory loss, particularly involving recent events or conversations, which may go unnoticed or be mistaken for normal aging. As the disease progresses, individuals experience more pronounced cognitive decline, including difficulties with language, problem-solving, and planning. Behavioral and psychological changes, such as increased anxiety, irritability, and depression, often accompany cognitive deterioration, affecting the individual's ability to interact socially and manage daily activities.

    Globally, Alzheimer's Disease is a significant public health concern. The World Health Organization (WHO) estimates that approximately 55 million people were living with dementia in 2021, with Alzheimer's Disease being the leading cause. The incidence of Alzheimer's Disease increases significantly with age, and nearly 10 million new cases of dementia are diagnosed each year worldwide. As the global population continues to age, the prevalence of Alzheimer's Disease is expected to rise dramatically, potentially reaching 139 million cases by 2050.

    Despite advances in research, there is currently no cure for Alzheimer's Disease. Available treatments focus on alleviating symptoms and slowing disease progression. Medications such as cholinesterase inhibitors and NMDA receptor antagonists can offer modest improvements in cognitive function and daily living activities, but they do not stop the underlying neurodegenerative process. The substantial economic burden of Alzheimer's Disease, including healthcare costs and the impact on families and caregivers, highlights the importance of economic evaluations in the development of new therapies.

    Cost-effectiveness analysis (CEA) and budget impact analysis (BIA) are crucial tools for assessing the value and affordability of emerging treatments. As potential disease-modifying therapies are developed, these evaluations will inform policymakers on how to allocate resources efficiently, ensuring that the most effective interventions are made accessible to those in need. The increasing prevalence of Alzheimer's Disease underscores the urgent need for continued research into preventive measures, innovative treatments, and supportive care strategies to mitigate its impact on individuals and societies worldwide.
    """)

elif page == "Natural History":
    st.title("Natural History of Alzheimer's Disease")
    st.write("Information about the progression of Alzheimer's Disease.")

elif page == "Simulation Conceptual Model":
    st.title("Simulation Model")
    st.write("Details of the simulation model used.")

elif page == "Run Economic Evaluation":
    st.title("Run Economic Evaluation")
    st.write("Run Economic Evaluation")

elif page == "Results":
    st.title("Results")
    st.write("Results")

elif page == "Publications":
    st.title("Publications")
    st.write("List of publications relevant to Alzheimer's disease.")
