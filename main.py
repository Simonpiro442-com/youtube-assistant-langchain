import streamlit as st
import langchain_helper as lch
from langchain_helper import get_response_from_query  # 👈 Add this
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="What is the Youtube video URL?",
            max_chars=50
        )
        query=st.sidebar.text_area(
            label="Ask me about the Video",
            max_chars=50,
            key="query"
        )

        submit_button=st.form_submit_button(label="Submit")

if query and youtube_url:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response, docs = get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width = 80))