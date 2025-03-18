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
        ("system", "You are a helpful assistant that can analyse images of nutrition."
                    "chart and help choosing right diet"),
        (
            "human",
            [
                {"type": "text", "text": "{input}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,""{image1}",
                        "detail": "low",
                    },
                },

                {"type": "text", "text": "{input}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,""{image2}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

chain = prompt | llm
uploaded_file1 = st.file_uploader("Upload your image1",type=["jpg","png"])
uploaded_file2 = st.file_uploader("Upload your image2",type=["jpg","png"])
question = st.text_input("Enter a question")

if question:
    image1=encode_image(uploaded_file1)
    image2=encode_image(uploaded_file2)
    response = chain.invoke({"input": question,"image1":image1,"image2":image2})
    st.write(response.content)