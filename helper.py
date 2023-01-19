from dotenv import load_dotenv
import os

import streamlit as st

@st.cache
def get_keys():
    """
    Gets the Cohere API key from the .env file
    :return: The key
    """
    load_dotenv()
    return os.getenv("COHERE_KEY"), os.getenv("AI21_KEY")