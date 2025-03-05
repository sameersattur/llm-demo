import os
from langchain_community.chat_models import ChatOllama
import streamlit as st
# from langchain.globals import set_debug
# set_debug(True)

llm = ChatOllama(model="gemma:2b")

st.title("ask anything")
question = st.text_input("What is your question? ")
if question:
    response = llm.invoke(question)
    st.write(response.content)