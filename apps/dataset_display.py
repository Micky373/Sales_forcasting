import streamlit as st
import pandas as pd

def app():
    st.title('In this page we display all the datasets')
    
    with st.spinner("Loading Data ..."):
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Data display page</p>", unsafe_allow_html=True)
     
        st.write("""
        The data contains historical sales data for 1,115 Rossmann stores. 
        """)
        st.markdown("The data and feature description for this challenge can be found [here](https://www.kaggle.com/c/rossmann-store-sales)")
 

        train = pd.read_csv('train_display.csv')
        st.write(train)
