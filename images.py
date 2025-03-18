from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import base64
import os


def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode()



llm = ChatOllama(model="llama3:latest")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can describe images."),
        (
            "human",
            [
                {"type": "text", "text": "{input}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,""{image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

chain = prompt | llm
uploaded_file = st.file_uploader("Upload your image",type=["jpg","png"])
question = st.text_input("Enter a question")

if question:
    image=encode_image(uploaded_file)
    response = chain.invoke({"input": question,"image":image})
    st.write(response.content)