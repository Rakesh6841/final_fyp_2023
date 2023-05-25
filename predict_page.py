import pickle
import numpy as np
import pandas as pd
import streamlit as st
import sklearn

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/ct.pkl', 'rb') as f:
    ct = pickle.load(f)

def show_predict_page():
    st.title("Instagram Reach Analysis & Prediction")
    categories = ("food", "photography", "dance", "sports")
    hours = list(range(24))
    category = st.selectbox("Category", categories)
    hour = st.selectbox("Time of Post", hours)
    follower = st.number_input("No. of Followers", step=1)
    post = st.number_input("No. of Posts", step=1)
    predicted_likes = model.predict(ct.transform([[category, hour, follower, post]]))
    predicted_likes = predicted_likes[0]*10  # Get the first element if it's a NumPy array

    ok = st.button("Predict Now")
    if ok:
        st.subheader("The predicted likes: {}".format(predicted_likes))