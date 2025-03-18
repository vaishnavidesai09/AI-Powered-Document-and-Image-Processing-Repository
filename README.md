# 🤖 AI Agents for Document & Image Analysis

## Overview
This repository contains various AI-powered applications built using LangChain, Ollama, and Streamlit. These AI agents can process text documents, analyze images, verify identification documents, and perform search-based retrieval for question-answering tasks.

## Features
- 📚 **Legal Document Analysis**: A RAG-based chatbot for answering questions from legal documents.
- 🌟 **AI-Powered Image Analysis**: Identify landmarks, analyze nutrition charts, and generate image descriptions.
- 👤 **KYC Verification**: Verifies identification details from uploaded documents.
- 🔍 **Search Agent**: Uses Wikipedia and DuckDuckGo to retrieve relevant information.

## Installation
🛠️ To use these AI agents, clone this repository and install the required dependencies:


## Usage
Each AI agent runs as a Streamlit app. Start any module using:
```bash
streamlit run script_name.py
```

## AI Agents

### 📖 Legal Document QA
- **Function**: Processes legal documents and provides answers using a Retrieval-Augmented Generation (RAG) model.
- **Libraries Used**: LangChain, HuggingFace Embeddings, ChromaDB, FAISS.
- **Run Command**:
  ```bash
  streamlit run rag.py
  ```

### 🌟 Nutrition Chart Analyzer
- **Function**: Analyzes nutrition charts from images and provides dietary recommendations.
- **Libraries Used**: LangChain, Ollama, Streamlit.
- **Run Command**:
  ```bash
  streamlit run nutrition.py
  ```

### 🌍 Landmark Identifier
- **Function**: Identifies landmarks from uploaded images.
- **Libraries Used**: LangChain, Ollama, Streamlit.
- **Run Command**:
  ```bash
  streamlit run landmark.py
  ```

### 📋 KYC Verification
- **Function**: Verifies identification documents with text and image inputs.
- **Libraries Used**: LangChain, Ollama, Streamlit.
- **Run Command**:
  ```bash
  streamlit run kyc.py
  ```

### 🔎 AI Search Agent
- **Function**: Fetches information from Wikipedia and DuckDuckGo based on user queries.
- **Libraries Used**: LangChain, Wikipedia API, DuckDuckGo Search.
- **Run Command**:
  ```bash
  streamlit run agent.py
  ```

## Contributing
🚀 Contributions are welcome! Feel free to submit pull requests or open issues.

## License
📚 This project is licensed under the MIT License.

---
🐝 Created by [Vaishnavi Desai](https://github.com/vaishnavidesai09)

