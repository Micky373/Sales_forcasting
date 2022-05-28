import streamlit as st

def app():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Rossmann Pharmaceuticals</p>", unsafe_allow_html=True)
    
        st.write(
            """
            Dirk Rossmann GmbH (usual: Rossmann) is one of the largest drug store chains in Europe with around 56,200 employees and more than 4000 stores across Europe.
                """
        )
        st.image('./home.jpg', use_column_width=True)
        st.write("""
        
         This app is an end-to-end solution that allows the Rosemann pharmaceutical company to see sales forecasts for its stores six weeks in advance, as well as expected trends.
         """)