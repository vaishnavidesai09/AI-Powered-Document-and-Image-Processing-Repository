import os
from langchain_ollama import ChatOllama
from langchain import hub
import streamlit as st
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOllama(model="llama3:latest")


prompt = hub.pull("hwchase17/react")
tools = load_tools(['wikipedia','ddg-search'])
agent = create_react_agent(llm,tools,prompt)
Agent_Executor= AgentExecutor(agent=agent,tools = tools, verbose=True)
st.title("Ai Agent")
task = st.text_input("Assign me a task")
if task:
    response=Agent_Executor.invoke({"input":task})
    st.write(response['output'])
