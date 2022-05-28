import streamlit as st
import pandas as pd

def app():
    st.title('In this page we display all the datasets')
    
    with st.spinner("Loading Data ..."):
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:2rem;border-radius:1rem;'>Data Display</p>", unsafe_allow_html=True)
     
        st.write("""
        The data contains historical sales data for 1,115 Rossmann stores. 
        """)
        st.markdown("The data and feature description for this challenge can be found [here](https://www.kaggle.com/c/rossmann-store-sales)")
 

        train = pd.read_csv('train.csv')
        store = pd.read_csv('store.csv')
        merged_train = pd.merge(left = train, right = store, how = 'inner', left_on = 'Store', right_on = 'Store')
        merged_train = merged_train.set_index('Store')
        st.write(merged_train)
