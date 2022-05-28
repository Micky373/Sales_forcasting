import streamlit as st
import pandas as pd

def app():
    st.title('In this page we display all the datasets')
    
    with st.spinner("Loading Data ..."):
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:2rem;border-radius:0.8rem;'>Data display page</p>", unsafe_allow_html=True)
     
        st.markdown("<p style='font-size:1.8rem'>The data contains historical sales data for 1,115 Rossmann stores.</p>", unsafe_allow_html=True)

        st.markdown("<p style='font-size:1.8rem'>The data and feature description for this challenge can be found https://www.kaggle.com/c/rossmann-store-sales</p>",unsafe_allow_html=True)
 

        train = pd.read_csv('./data/train_display.csv')
        st.write(train)
