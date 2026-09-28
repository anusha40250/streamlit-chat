import streamlit as st
from ollama import chat
st.title("My AI Bot: Synora")
name = "Anusha"
st.write("welcome,",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    # st.write("You asked:", question)
    response = chat(model="gemma3:1b", messages=[{
        "role": "system",
        "content": "you are a firendly tutor. You explain concepts in a simple way.Explain concepts in 50 words max."
        },
        {
            "role": "user",
            "content": question
        }])
    answer = response.message.content
    st.write(answer)
# #dropdown
# options = ["c++", "python", "java"]
# choice = st.selectbox("select your favorite programming language:", options)
# st.write(f"You selected: {choice}")