from rag import get_answer
import streamlit as st

question = st.text_input("Enter a prompt?")

if question.strip():
    st.write(get_answer(question))