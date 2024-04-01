import streamlit as st
import requests
from requests import Response

url = "http://localhost:5000/shorten" 

st.title("Welcome to Dwarf")
st.write("Shorten your long scary urls into simple short hash-type format")
url_input = st.text_input("Enter your URL here:")


def make_request(long_url: str)->Response:
    payload = {
        "url": long_url
    }
    response = requests.post(url, json=payload)
    return response


if st.button("Shorten"):
    if url_input and url_input.startswith(("http://", "https://")):
        response = make_request(long_url=url_input)
        response_data = response.json()
        if response_data["status_code"] == 200:
            short_url = response_data["short_url"]
            st.success(f"Shortened URL: {short_url}")
        else:
            status_code = response_data["status_code"]
            msg = response_data["message"]
            st.error(f"Error code: {status_code}, Message - {msg}")
    else:
        st.error("Please enter a valid URL.")
