import streamlit as st
from multiapp import MultiApp
from apps import dataset_display,home_page,insight,predict_query,prediction_display # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **Pharmaceutical Sales forcasting**')
st.sidebar.markdown("""
The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality.

""")

# Add all your application here
app.add_app("Home page", home_page.app)
app.add_app("Data sets", dataset_display.app)
app.add_app("Insights", insight.app)
app.add_app("Predicting page", predict_query.app)
app.add_app("Prediction display", prediction_display.app)
# The main app
app.run()