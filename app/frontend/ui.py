import streamlit as st
import requests
from requests import Response

url = "http://localhost:5000/shorten" 

st.title("Welcome to Dwarf")
st.write("Intro")
url_input = st.text_input("Enter your URL here:")


def make_request(long_url: str)->Response:
    data = {"url": long_url}
    response = requests.post(url, json=data)
    return response


if st.button("Shorten"):
    if url_input:
        response = make_request(long_url=url_input)
        if response.status_code == 200:
            short_url = response.json()["short_url"]
            st.success(f"Shortened URL: {short_url}")
        else:
            st.error(f"Error while shortening URL")
    else:
        st.error("Please enter a valid URL.")
