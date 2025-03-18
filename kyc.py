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
        ("system", "You are a helpful assistant that can verify identification documents."),
        (
            "human",
            [
                {"type": "text", "text": "Verify the identification details."},
                {"type": "text", "text": "Name: {user_name}"},
                {"type": "text", "text": "DOB: {user_dob}"},
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
st.title("KYC Verification Application")
st.write("upload your identification document")
uploaded_file = st.file_uploader("Upload your document",type=["jpg","png"])

user_name = st.text_input("Enter your user name")
user_dob = st.text_input("Enter your Date of birth")
if uploaded_file is not None and user_name and user_dob:
    image=encode_image(uploaded_file)
    response = chain.invoke({"user_name":user_name,"user_dob":user_dob ,"image":image})
    st.write(response.content)