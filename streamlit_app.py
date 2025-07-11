import streamlit as st
from scraper import scrape_race_data
from predictor import predict_top_4

st.title("🐾 Greyhound Race Predictor")

url = st.text_input("Paste TheDogs race URL:")

if url:
    data = scrape_race_data(url)
    st.dataframe(data)

    top_4 = predict_top_4(data)
    st.markdown("### 🏆 Predicted Top 4 Finishers:")
    for i, dog in enumerate(top_4, start=1):
        st.write(f"{i}. {dog}")
