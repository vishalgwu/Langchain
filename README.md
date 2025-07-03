# Langchain

A comprehensive Python-based repository to explore, prototype, and experiment with LangChain concepts, including LLMs, embeddings, retrieval-augmented generation (RAG), chains, output parsers, and Streamlit-based chatbot interfaces. This project serves as a modular sandbox for experimenting with LangChain features, agent tools, and modern retrieval architectures.

---

## 🚀 Project Overview

This project demonstrates an end-to-end framework for building, running, and testing various LangChain pipelines and concepts. It covers:

- Large Language Models (LLMs)
- Embedded Models
- Retrieval-Augmented Generation (RAG)
- Runnable patterns (Passthrough, Sequence, Parallel)
- Chains (conditional, sequential, parallel)
- Output parsers with Pydantic schemas
- Streamlit-based user interfaces
- Chat model integrations (OpenAI, Hugging Face, Claude, etc.)

The repository is modular, making it easy to extend, plug in new models, and explore LangChain use cases with a clear directory structure.

---

## 📁 Folder Structure

```text
Langchain/
├── EmbeddedModels/
│   ├── hugging_face1.py
│   ├── huginf_face_local.py
│   ├── open_ai_doc.py
│   └── open_ai.py
├── LLMs/
│   └── llm_demo.py
├── Rags/
│   ├── agents/
│   │   ├── agent.py
│   │   └── tools.py
│   ├── document_loader/
│   │   ├── business.txt
│   │   ├── directory_loader.py
│   │   ├── Hessian_Examples.pdf
│   │   ├── pdf_loader.py
│   │   ├── text_loader.py
│   │   ├── web_base_loader.py
│   │   └── wikipedia.cpython-312.pyc
│   ├── Retrivers/
│   │   └── __pycache__/
│   ├── Text_splitter/
│   │   ├── code_splitter.py
│   │   ├── length_based.py
│   │   ├── length_bases_pdf.py
│   │   ├── markdown_splitter.py
│   │   └── text_based.py
│   ├── Youtube_chatbot.py
│   └── ...
├── Runnable/
│   ├── Runnable.py
│   ├── Runnable_passthrough.py
│   ├── Runnable_parallel.py
│   └── Runnable_sequence.py
├── Streamelit/
│   ├── chatbot_command.py
│   ├── chatbot_st.py
│   ├── prompt_dynamic_minmax_2.py
│   ├── prompt_dynamic_minmax.py
│   ├── prompt_meloni.py
│   └── prompt_minmax.py
├── chains/
│   ├── conditional_chain.py
│   ├── parallel_chain.py
│   └── seq_chain.py
├── chatModels/
│   ├── chat_model_claud.py
│   ├── chat_model_google.py
│   ├── chat_model_hugging_face_local.py
│   ├── chat_model_hugging_face.py
│   └── chat_model_openai.py
├── output_parsers/
│   ├── string_output_json_chain.py
│   ├── string_output_json.py
│   ├── string_output_openai.py
│   ├── string_output_parser_chain.py
│   ├── string_output_parsers.py
│   ├── string_pydantic_output.py
│   ├── string_str_output_json_chain.py
│   └── string_structured_output.py
├── structured_output/
│   ├── json_str.json
│   ├── pydantic_demo.py
│   ├── str_output_dict.py
│   └── structured_output.py
├── .env
├── req.txt
└── README.md


## 📂 Folder Explanations

- **EmbeddedModels/**: Contains scripts to work with embedding models like Hugging Face and OpenAI.  
- **LLMs/**: Demonstrations of prompt-based LLM interactions.  
- **Rags/**: Retrieval-Augmented Generation modules including agents, document loaders, text splitters, retrievers, and YouTube chatbot examples.  
- **Runnable/**: Runnable patterns for chaining and controlling LLM operations.  
- **Streamelit/**: Streamlit-based chat interfaces and prompt experiments.  
- **chains/**: Conditional, parallel, and sequential chain orchestration examples.  
- **chatModels/**: Integration scripts for various chat providers (OpenAI, Claude, Hugging Face, Google).  
- **output_parsers/**: Includes pydantic-based and JSON-based parsing for LLM outputs.  
- **structured_output/**: Examples of structured output management, including Pydantic and JSON serialization.  
- **.env**: Environment variables file (add your own keys here, do not commit to GitHub).  
- **req.txt**: Lists the Python dependencies to install.  

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/vishalgwu/Langchain.git
cd Langchain

## Create a virtual environment-
python -m venv venv

## Activate the environment

On Windows:venv\Scripts\activate

On macOS/Linux:

bash
source venv/bin/activate

Install dependencies:
pip install -r req.txt

## API Keys & Environment Variables-
Copy the .env file provided, or create your own .env file in the root of the project.

Add your own API keys and secrets to the .env file, for example:
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
