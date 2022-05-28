import streamlit as st

def app():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Insights inferred from the data</p>", unsafe_allow_html=True)
    
        st.markdown("<p style='font-size:1.8rem'>The data has a number of important attributes that can be used to get insight into retail sales. The following conclusions can be drawn based on the exploratory data analysis: The volume of sales is proportional to the number of clients.</p>", unsafe_allow_html=True)