from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai

"""
# Image Recognition App

Multifile upload and recognition
"""


with st.echo(code_location='below'):
    uploaded_files = st.file_uploader("Upload images", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
    


def hello_world():
    
    openai.organization = st.secrets["OPENAI_ORG"]
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        messages=[
                {"role": "user", "content": "what is devops"},
            ]
    )

    return response