import streamlit as st
import requests

st.title('Market Sentiment Analysis')

text_input = st.text_area("Enter text to analyze sentiment:")

if st.button("Analyze"):
    response = requests.post("http://localhost:5000/predict", json={"text": text_input})
    sentiment = response.json()['sentiment']
    st.write(f"Sentiment: {sentiment}")
