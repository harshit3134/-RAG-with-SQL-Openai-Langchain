from langchain_final import get_answer
import streamlit as st

st.set_page_config(
    page_title="RAG Student-bot",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('🤖 RAG Student Bot')
st.write("Welcome to RAG Bot! Ask any question, and I'll provide answers.")

with st.sidebar:
    st.markdown("### Instructions")
    st.success('👉 Enter your question in the input box on the left and click Enter.')

question = st.text_input("Ask a Question:", "")
button_pressed = st.button("Get Answer", key="get_answer_button")

if button_pressed:
    if question:
        answer = get_answer(question)
        st.subheader("Answer:")
        st.info(answer)

