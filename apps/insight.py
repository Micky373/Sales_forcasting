import streamlit as st

def app():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Insights inferred from the data</p>", unsafe_allow_html=True)
    
        st.markdown("""
        The data has a lot of useful features that can provide insights into the stores sales. Based on the exploratory data analysis conducted, the following conclusions can be made: 
        `The number of customers` is directly related to the volume of sales.        
        """)