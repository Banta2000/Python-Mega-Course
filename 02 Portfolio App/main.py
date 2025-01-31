import streamlit as st
import pandas
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Manuel Altermatt")
    content = """
    Hi, I'm Manuel Altermatt, a software engineer with a passion for data science and machine learning."""
    st.info(content)

st.write(
    """
Here are some of the projects I have worked onlk jasdlk jaslk jasdlkj asdlökj alökdj alkösd. blablablas kdlsadlkj asdlkj asldkj aslkdj alkdsj salkdj l:
"""
)

st.write("### Project 1")
st.write("Description of project 1")

st.write("### Project 2")
st.write("Description of project 2")
